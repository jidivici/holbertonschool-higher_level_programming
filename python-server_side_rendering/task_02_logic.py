#!/usr/bin/python3
"""Flask app with dynamic content using Jinja loops."""

import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
        items_list = data.get("items", [])
        return render_template('items.html', items=items_list)
    except FileNotFoundError:
        return "Items file not found", 404
    except json.JSONDecodeError:
        return "Error decoding JSON", 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
