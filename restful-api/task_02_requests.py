#!/usr/bin/python3
"""Fetches posts from JSONPlaceholder API and saves them to a CSV file."""
import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder API and print their titles."""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()
        print("Status Code: {}".format(response.status_code))
        posts = response.json()
        for post in posts:
            print("{}".format(post["title"]))
    except requests.exceptions.RequestException as e:
        print("Erreur de requête : {}".format(e))


def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder API and save them to posts.csv."""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()
        posts = response.json()

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            filtered_posts = [
                {"id": post["id"], "title": post["title"],
                 "body": post["body"]}
                for post in posts
            ]
            writer.writerows(filtered_posts)
    except requests.exceptions.RequestException as e:
        print("Bad request: {}".format(e))
    except IOError as e:
        print("Access denied: {}".format(e))
