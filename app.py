from matplotlib import ticker
from User import User
from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from werkzeug.middleware.profiler import ProfilerMiddleware
import json
from Stack import Stack
from Queue import Queue


templates = FileSystemLoader('templates')
environment = Environment(loader=templates)

app = Flask(__name__)
app.static_folder = './templates/static'

app.config['PROFILE'] = True

waitList = Queue()


def getConcerts():
    file = open('concertInfo.json')
    data = json.load(file)
    file.close()
    return data


def generateTicketCode(name, loc_name):
    code = ''
    for letter in name.split():
        code = code + letter[0]
    code = code + loc_name.replace(' ', '-')
    return code


@app.route('/', methods=["GET", "POST"])
def landingPage():
    return render_template('landingPage.html')


@app.route('/signup', methods=["GET", "POST"])
def createAccount():
    if request.method == 'POST':
        name = request.form['name']
        l_name = request.form['last_name']
        username = request.form['username']
        mail = request.form['email']
        password = request.form['password']
        newUser = User(name, l_name, username, mail, password)
        return redirect(f'/{newUser.username}')
    return render_template('signUp.html')


@app.route('/<username>', methods=["GET", "POST"])
def homePage(username):
    return render_template('homePage.html', username=username)


@app.route('/<username>/events', methods=["GET"])
def concerts(username):
    concerts = getConcerts()
    return render_template('concertsPage.html', username=username, concerts=concerts)


@app.route('/<username>/<id>', methods=["GET"])
def event(username, id):
    concerts = getConcerts()
    return render_template('event.html', username=username, id=int(id), concerts=concerts)


@app.route('/<username>/buyTicket/<fest_id>/<loc_id>', methods=["GET", "POST"])
def buyTicket(username, fest_id, loc_id):
    concerts = getConcerts()
    concert_name = concerts[int(fest_id)]['name']
    location_name = concerts[int(fest_id)]['locations'][int(loc_id)]
    ticket_code = generateTicketCode(concert_name, location_name)
    buy_info = (username, ticket_code)
    waitList.enqueue(buy_info)
    return render_template('waitingList.html', username=username)


@app.route('/<username>/post', methods=["GET", "POST"])
def newConcert(username):
    return render_template('addConcert.html', username=username)


if __name__ == "__main__":
    # app.wsgi_app = ProfilerMiddleware(app.wsgi_app)
    app.run(debug=True)
