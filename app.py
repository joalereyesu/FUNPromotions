from crypt import methods
from User import User
from email.policy import default
from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
import numpy as np


templates = FileSystemLoader('templates')
environment = Environment(loader=templates)

app = Flask(__name__)
app.static_folder = './templates/static'


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
    return render_template('concertsPage.html', username=username)


@app.route('/<username>/<id>', methods=["GET"])
def event(username, id):
    print(type(id))
    return render_template('event.html', username=username, id=int(id))


@app.route('/<username>/post', methods=["GET", "POST"])
def newConcert(username):
    return render_template('addConcert.html', username=username)


if __name__ == "__main__":
    app.run(debug=True)
