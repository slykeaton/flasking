from lib2to3.pgen2 import token
import re
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
from datetime import date

currentTime = datetime.datetime.utcnow()

app = Flask(__name__)

import os

file_path = os.path.abspath(os.getcwd())+"\database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
db = SQLAlchemy(app)

class Token(db.Model):
    token = db.Column(db.Integer, unique = True, primary_key=True)
    expiration = db.Column(db.DateTime)

    def __repr__(self):
        return '<Token %r>' % self.token

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def hello_world():
    return render_template('landing.html')

@app.route("/auth")
def test_auth():
    givenToken = request.args.get('token', '')
#    tokenCheck = Token.query.filter_by(token=givenToken).first()
#    dateCheck = Token.query.filter_by(expiration)
    return db.query.all()
#    return "You have passed the token check with token " + givenToken + ". The current time is " + currentTime.strftime("%m/%d/%Y, %H:%M:%S") +" UTC."