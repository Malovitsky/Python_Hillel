import requests
import flask
import faker
import datetime
import random
from flask import Flask, render_template
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
@app.route("/password")
@use_kwargs({
    "length": fields.Int(
        required=True,

        validate=[validate.Range(min=1, max=100)]
    ),
    "specials": fields.Int(
        required=False,
        validate=[validate.OneOf([0, 1])]
    ),
    "digits": fields.Int(
        required=False,
        validate=[validate.OneOf([0, 1])]
    )},
    location="query"
)
def pass_gen(**kwargs):
    specials = kwargs.get('specials', False)
    digits = kwargs.get('digits', False)

    random_base = string.ascii_lowercase + string.ascii_uppercase

    if specials:
        random_base += string.punctuation
        return ''.join(random.choices(random_base, k=kwargs['length']))
    if digits:
        random_base += string.digits
        return ''.join(random.choices(random_base, k=kwargs['length']))
    else:
        return "".join(random.choices(random_base, k=kwargs['length']))


@app.route("/bitcoin_rate")
@use_kwargs({
    "currency": fields.Str(
        required=False,

        validate=[validate.ContainsOnly("UAH")]
    )
},
    location="query"
)
def get_bitcoin_rate(**kwargs):
    currency = kwargs.get('currency')
    print(currency)
    headers = {
        'content-type': 'application/json;charset=utf-8',
        'User-Agent': 'Python'

    }

    url = "https://bitpay.com/api/rates"

    request_to_url = requests.get(url, headers=headers)

    if currency:
        for element in request_to_url.json():
            if element["code"] == currency:
                return render_template('index_currency.html', name=str(element))
    else:
        for element in request_to_url.json():
            if element["code"] == "USD":
                return render_template('index_currency.html', name=str(element))


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
#print(dir(e))
sequens = [string.punctuation+string.ascii_lowercase]
#print(sequens)

app.run(debug=True)
