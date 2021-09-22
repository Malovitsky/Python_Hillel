import requests
import flask
import faker
import datetime
import random
from flask import Flask
import string
from flask import request
from marshmallow import validate
from webargs import fields
from webargs.flaskparser import use_kwargs


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello():
    return "<p>Hello, Hillel!</p>"


@app.route("/now")
def get_current_time():
    return str(datetime.datetime.now())



@app.route("/get_random_students")
def get_random_students():
    random_students_list = []
    x = faker.Faker("UK")
    for i in range(1, 10):
        random_students_list.append(x.first_name() + " " + x.last_name())
    return str(random_students_list)

@app.route("/get_pipenv")
def get_pipenv():
    with open("./Pipfile.lock", "r") as file:
        e = file.read()
        return e
e = string
sequens = [string.punctuation+string.ascii_lowercase]


app.run(debug=True)
