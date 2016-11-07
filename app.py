#!/usr/bin/python

from flask import Flask
from flask import render_template
from flask import request

import json
import random

app = Flask(__name__)

quotes = []

with open('data.json', 'r') as f:
    quotes = json.loads(f.read())

@app.route('/')
def index():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

@app.route('/search')
def search():
    q = request.args.get('q')

    for quote in quotes:
        if q.lower() in quote['quote'].lower():
            return render_template('search.html', q=q, quote=quote)

    return render_template('search.html', q=q)

app.run()