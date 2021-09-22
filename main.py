import random
from flask import Flask, render_template
import string
from marshmallow import validate
from webargs import fields
from webargs.flaskparser import use_kwargs
import requests

app = Flask(__name__, template_folder="templates")


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


app.run(debug=True, port=5001)
