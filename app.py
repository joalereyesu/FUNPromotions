from User import User
from flask import Flask, render_template, request, url_for, redirect, jsonify, Response
from jinja2 import Template, FileSystemLoader, Environment
from werkzeug.middleware.profiler import ProfilerMiddleware
import json
from Stack import Stack
from Queue import Queue
from BinaryTree import Tree
from datetime import datetime
from Graph import Graph
import firebase_admin
import pyrebase
from firebase_admin import credentials, auth
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO

# CONNECTION TO FIREBASE
cred = credentials.Certificate('fbAdminConfig.json')
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))


templates = FileSystemLoader('templates')
environment = Environment(loader=templates)

app = Flask(__name__)
app.static_folder = './templates/static'

app.config['PROFILE'] = True

concertsTree = Tree()

datestamps = []
file = open('concertInfo.json')
data = json.load(file)
for concert in data:
    strDate = concert['date']
    date = datetime.strptime(strDate, "%B %d, %Y")
    datestamp = int(datetime.timestamp(date))
    datestamps.append(datestamp)
    concert['date'] = int(datestamp)
    concertsTree.insert(concert)
file.close()

waitList = Queue()
ticketsSold = Stack()
usersDistribution = Graph()

usersExample = ['marcemelgar', 'nickonolte',
                'estebanquarzo', 'fboiton', 'danielb', 'mariops']
festCodesExample = ['SMFFINE-LINE', 'LIEL-MADRILEÑO',
                    'HSTIMELEZZ', 'CFSOUR', 'CFHELLO', 'LISAOKO']


for x in range(len(usersExample)):
    exampleTuple = (usersExample[x], festCodesExample[x])
    waitList.enqueue(exampleTuple)
    ticketsSold.push(exampleTuple)

print(f"QUEUE INICIAL: {waitList.show()}")
print(len(waitList.show()))
print(f"STACK INICIAL: {ticketsSold.getStackAsList()}")


def getConcerts():
    file = open('concertInfo.json')
    data = json.load(file)
    file.close()
    return data


def getTicketInfo(id):
    concerts = getConcerts()
    for concert in concerts:
        codes = concert['codes']
        for code in codes:
            if code == id:
                return concert


def generateTicketCode(name, loc_name):
    code = ''
    for letter in name.split():
        code = code + letter[0]
    code = code + loc_name.replace(' ', '-')
    return code


graphsConcertExample = getConcerts()
for concert in graphsConcertExample:
    usersDistribution.add_node(concert['name'])
    for code in concert['codes']:
        usersDistribution.add_node(code)
        usersDistribution.add_edge(concert['name'], code)

for i in range(len(usersExample)):
    usersDistribution.add_node(usersExample[i])
    usersDistribution.add_edge(festCodesExample[i], usersExample[i])


@app.route('/', methods=["GET", "POST"])
def landingPage():
    if request.method == "POST":
        username = request.form.get('username')
        mail = request.form.get('email')
        password = request.form.get('password')
        try:
            user = pb.auth().sign_in_with_email_and_password(mail, password)
            print(user)
            jwt = user['idToken']
            return redirect(f'/{username}')
        except:
            return {'message': 'There was an error loging in'}, 400
    return render_template('landingPage.html')


@app.route('/signup', methods=["GET", "POST"])
def createAccount():
    if request.method == 'POST':
        name = request.form.get('name')
        l_name = request.form.get('last_name')
        username = request.form.get('username')
        mail = request.form.get('email')
        password = request.form.get('password')
        newUser = User(name, l_name, username, mail, password)
        try:
            user = auth.create_user(
                email=mail,
                password=password
            )
            return redirect(f'/{newUser.username}')
        except:
            return {'message': 'Error creating user'}, 400
    return render_template('signUp.html')


@app.route('/<username>', methods=["GET", "POST"])
def homePage(username):
    return render_template('homePage.html', username=username)


@app.route('/<username>/events', methods=["GET"])
def concerts(username):
    concerts = getConcerts()
    concertsTree.inorder()
    return render_template('concertsPage.html', username=username, concerts=concerts, datestamps=datestamps)


@app.route('/<username>/<datestamp>/<id>', methods=["GET"])
def event(username, datestamp, id):
    selectedConcert = concertsTree.find(int(datestamp))
    print(selectedConcert)
    date = datetime.fromtimestamp(
        selectedConcert['date']).strftime("%B %d, %Y")
    print(selectedConcert)
    concertsTree.inorder()
    return render_template('event.html', username=username, id=int(id), concert=selectedConcert, date=date)


@app.route('/<username>/<datestamp>/waitlist/<loc_id>', methods=["GET", "POST"])
def waitlist(username, datestamp, loc_id):
    selectedConcert = concertsTree.find(int(datestamp))
    print(selectedConcert)
    concert_name = selectedConcert['name']
    location_name = selectedConcert['locations'][int(loc_id)]
    ticket_code = generateTicketCode(concert_name, location_name)
    buy_info = (username, ticket_code)
    waitList.enqueue(buy_info)
    return render_template('waitingList.html', username=username)


@app.route('/waitingList/<username>', methods=['GET'])
def waitingList(username):
    pendingList = waitList.show()
    if request.method == 'GET':
        waitList.dequeue()
        data = {
            "waitList": waitList.show(),
            "pendingUsers": str(waitList.size()),
            'stop': False
        }
        print(pendingList)
        print(len(pendingList))
        if (len(pendingList) == 1 and pendingList[0][0] == username):
            data['stop'] = True
            return jsonify(data)
        return jsonify(data)
    else:
        return page_not_found(404)


@app.route('/buyTicket/<username>/<fest_id>', methods=['GET', 'POST'])
def buyTicket(username, fest_id):
    selectedConcert = concertsTree.find(int(datestamp))
    print(selectedConcert)
    date = datetime.fromtimestamp(
        selectedConcert['date']).strftime("%B %d, %Y")
    return render_template('buyTickets.html', username=username, fest_id=fest_id, concertData=selectedConcert, date=date)


@app.route('/<username>/<fest_id>/success', methods=['GET', 'POST'])
def saveBuy(username, fest_id):
    ticketsSold.push((username, fest_id))
    usersDistribution.add_node(username)
    usersDistribution.add_edge(fest_id, username)
    usersDistribution.disp_graph()
    print(f"STACK INSERTANDO ELEMENTO: {ticketsSold.getStackAsList()}")
    return render_template('success.html', username=username)


@app.route('/cancelTicket/<username>', methods=['GET', 'POST'])
def cancelTicket(username):
    ticketsSold.pop()
    print(f"STACK ELIMINANDO ELEMENTO: {ticketsSold.getStackAsList()}")
    return {"success": True}


@app.route('/getStacks/<username>', methods=['GET'])
def getStacks(username):
    if request.method == 'GET':
        userInfo = ticketsSold.peek()
        return {
            "username": userInfo[0],
            "fest_id": userInfo[1]
        }


@app.route('/<username>/post', methods=["GET", "POST"])
def newConcert(username):
    return render_template('addConcert.html', username=username)


plt.rcParams["figure.figsize"] = [20, 12]
plt.rcParams["figure.autolayout"] = True


@app.route('/admin/seeUsers', methods=['GET'])
def seeUsers():
    G = nx.DiGraph()
    G.add_edges_from(usersDistribution.getAllRelations())
    vals = []
    val_map = {}
    x = 10.0
    for element in usersDistribution.getAllRelations():
        vals += element[0]
    values = [val_map.get(node, 0.80) for node in G.nodes()]
    black_edges = [edge for edge in G.edges()]
    cmap = matplotlib.colors.ListedColormap(['C0', 'blue'])
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color=values,
                           node_size=5000, cmap=cmap)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    output = BytesIO()
    plt.savefig(output)
    output.seek(0)
    plt.clf()
    return Response(output.getvalue(), mimetype='image/png')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_found.html'), 404


if __name__ == "__main__":
    # app.wsgi_app = ProfilerMiddleware(app.wsgi_app)
    app.run(debug=True)
