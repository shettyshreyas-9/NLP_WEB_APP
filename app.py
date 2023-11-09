from flask import Flask, render_template, request, redirect
from db import Database

from api import API

app = Flask(__name__)

dbo= Database()

apio= API()

@app.route('/')

def index():
    return render_template('login.html')


@app.route('/register')

def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name= request.form.get('user_name')
    email= request.form.get('user_email')
    password= request.form.get('user_password')

    response= dbo.insert(name,email,password)
    if response:
        return render_template('login.html', message='Registration successful. Kindly login to proceed')
    else:
        return render_template('register.html', message='Email already exists')

    # return name +" " +email +" " +password


@app.route('/perform_login', methods=['post'])
def perform_login():
    email= request.form.get('user_email')
    password= request.form.get('user_password')

    response= dbo.search(email,password)
    if response==1:
        return redirect('/profile')
    else:
        return render_template('login.html', message='Incorrect email/password')


@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')


@app.route('/perform_ner', methods=['post'])
def perform_ner():
    text = request.form.get('ner_text')
    response = apio.ner(text)
    print(response)


    return render_template('ner.html',response=response)

app.run(debug=True)