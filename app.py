from crypt import methods
from User import User
from Concert import Concert
from db import getConcerts
from email.policy import default
from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment


templates = FileSystemLoader('templates')
environment = Environment(loader=templates)

app = Flask(__name__)
app.static_folder = './templates/static'

names = ['HOLY SUMMER', 'LA ISLA', 'SPOOKY MONSTER FESTIVAL']

lineups = [
    ['Bad Bunny', 'Rauw Alejandro', 'Jhay Cortez', 'Jay Wheeler'],
    ['C. Tangana', 'Rels B', 'Rosalia', 'Humbe', 'Sebastian Cortes'],
    ['Dua Lipa', 'Doja Cat', 'Harry Styles', 'Bruno Mars', 'Lady Gaga', 'The Weeknd']]

capacity = ['50000', '30550', '90800']

price = [['1000', '1500', '2000', '2500'],
         ['850', '1300', '1700', '2300'],
         ['1250', '1750', '2100', '3400']]

location = [['PLATONICOS', 'TIMELEZZ', 'VICE VERSA', 'YHLQMDLG'],
            ['SAOKO', 'ENTROPIA', 'LA ISLA', 'EL MADRILEÑO'],
            ['PLANET HER', 'THE FAME', 'DAWN FM', 'FINE LINE']]

dates = ['April 16 2022', 'July 1 2022', 'October 29 2022']
time = ['12:00AM', '3:00PM', '11:30AM']

place = ['Puerto San Jose', 'Finca Gutierres', 'Finca Jocotillo']


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
        print(newUser)
        return redirect(f'/{newUser.username}')
    return render_template('signUp.html')


@app.route('/<username>', methods=["GET", "POST"])
def homePage(username):
    return render_template('homePage.html', username=username)


@app.route('/<username>/concerts', methods=["GET"])
def concerts(username):
    return render_template('concertsPage.html', username=username)


if __name__ == "__main__":
    app.run(debug=True)
