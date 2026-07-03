#!/usr/bin/env python3
"""Flask app reading products from JSON or CSV files."""

import json
import csv
from flask import Flask, render_template, request

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
    with open('items.json', 'r') as file:
        data = json.load(file)
    items_list = data.get("items", [])
    return render_template('items.html', items=items_list)


def read_json(filepath):
    """Read and parse a JSON file containing products."""
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data


def read_csv(filepath):
    """Read and parse a CSV file containing products."""
    products = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = {
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            }
            products.append(product)
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv'):
        return render_template(
            'product_display.html', error="Wrong source"
        )

    try:
        if source == 'json':
            data = read_json('products.json')
        else:
            data = read_csv('products.csv')
    except FileNotFoundError:
        return render_template(
            'product_display.html', error="File not found"
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error="Invalid id"
            )
        filtered = [p for p in data if p.get("id") == product_id]
        if not filtered:
            return render_template(
                'product_display.html', error="Product not found"
            )
        data = filtered

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
