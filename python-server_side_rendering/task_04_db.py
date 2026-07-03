#!/usr/bin/python3
"""Flask app reading products from JSON, CSV, or SQLite."""

import json
import csv
import sqlite3
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
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
        items_list = data.get("items", [])
        return render_template('items.html', items=items_list)
    except FileNotFoundError:
        return "Items file not found", 404
    except json.JSONDecodeError:
        return "Error decoding JSON", 500


def read_json(filepath):
    """Read and parse a JSON file of products."""
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data


def read_csv(filepath):
    """Read and parse a CSV file of products."""
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


def read_sql(dbpath):
    """Read products from a SQLite database."""
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(
        'SELECT id, name, category, price FROM Products'
    )
    rows = cursor.fetchall()
    conn.close()
    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
        return render_template(
            'product_display.html', error="Wrong source"
        )

    try:
        if source == 'json':
            data = read_json('products.json')
        elif source == 'csv':
            data = read_csv('products.csv')
        else:
            data = read_sql('products.db')
    except FileNotFoundError:
        return render_template(
            'product_display.html', error="File not found"
        )
    except json.JSONDecodeError:
        data = []
    except sqlite3.Error as e:
        return render_template(
            'product_display.html',
            error="Database error: {}".format(e)
        )
    except (ValueError, KeyError):
        return render_template(
            'product_display.html', error="Invalid data"
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error="Invalid id"
            )
        filtered = []
        for p in data:
            if p.get("id") == product_id:
                filtered.append(p)
        if not filtered:
            return render_template(
                'product_display.html', error="Product not found"
            )
        data = filtered

    return render_template(
        'product_display.html', products=data
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
