from User import User
from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from werkzeug.middleware.profiler import ProfilerMiddleware


templates = FileSystemLoader('templates')
environment = Environment(loader=templates)

app = Flask(__name__)
app.static_folder = './templates/static'

app.config['PROFILE'] = True


@app.route('/', methods=["GET", "POST"])
def landingPage():
    return render_template('landingPage.html')


@app.route('/signup', methods=["GET", "POST"])
def createAccount():
    if request.method == 'POST':
        name = request.args.get('name')
        l_name = request.args.get('last_name')
        username = request.args.get('username')
        mail = request.args.get('email')
        password = request.args.get('password')
        newUser = User(name, l_name, username, mail, password)
        return redirect(f'/{newUser.username}')
    return render_template('signUp.html')


@app.route('/<username>', methods=["GET", "POST"])
def homePage(username):
    return render_template('homePage.html', username=username)


@app.route('/<username>/events', methods=["GET"])
def concerts(username):
    return render_template('concertsPage.html', username=username)


@app.route('/<username>/<id>', methods=["GET"])
def event(username, id):
    print(type(id))
    return render_template('event.html', username=username, id=int(id))


@app.route('/<username>/post', methods=["GET", "POST"])
def newConcert(username):
    return render_template('addConcert.html', username=username)


if __name__ == "__main__":
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app)
    app.run(debug=True)
