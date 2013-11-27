#!flask/bin/python
from flask import Flask, jsonify
from flask.helpers import make_response
from scrapy import get_latest_petrol_price
from urls import get_petrol_url

app = Flask(__name__)

def all_prices(self):
    pass

def init(self):
    pass

@app.route('/fuelprice/v1.0/petrol/', methods=['GET'])
def get_petrol_prices_all():
    init()
    return all_prices()


@app.route('/fuelprice/v1.0/petrol/<string:city_name>', methods=['GET'])
def get_petrol_price(city_name):
    init()
    url = get_petrol_url(city_name)
    price = get_latest_petrol_price(url)
    return make_response(jsonify({ 'city' : city_name.title(), 'price' : price}))
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({ 'error': 'Not found'}))

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
