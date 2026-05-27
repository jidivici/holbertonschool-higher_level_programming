#!/usr/bin/env python3
"""Module to convert CSV data to JSON."""
import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON and save it as data.json list of dictionnaries."""
    try:
        data = []

        with open(filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except Exception:
        return False
