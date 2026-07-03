#!/usr/bin/env python3
"""Simple templating program generating invitation files."""

import os


def generate_invitations(template, attendees):
    """Generate invitation files from template and attendees.

    Args:
        template (str): The template string with placeholders.
        attendees (list): A list of dictionaries with attendee data.
    """
    if not isinstance(template, str):
        print("Invalid input: template must be a string, "
              "got {}".format(type(template).__name__))
        return

    if not isinstance(attendees, list):
        print("Invalid input: attendees must be a list, "
              "got {}".format(type(attendees).__name__))
        return

    for i, attendee in enumerate(attendees):
        if not isinstance(attendee, dict):
            print("Invalid input: attendee at index {} "
                  "must be a dictionary".format(i))
            return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template
        for key in ["name", "event_title",
                    "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        filename = "output_{}.txt".format(index)

        if os.path.exists(filename):
            print("{} already exists, skipping.".format(filename))
            continue

        try:
            with open(filename, "w") as file:
                file.write(output)
        except IOError as e:
            print("Error writing to {}: {}".format(filename, e))


if __name__ == "__main__":
    with open("template.txt", "r") as file:
        template_content = file.read()

    attendees = [
        {"name": "Alice",
         "event_title": "Python Conference",
         "event_date": "2023-07-15",
         "event_location": "New York"},
        {"name": "Bob",
         "event_title": "Data Science Workshop",
         "event_date": "2023-08-20",
         "event_location": "San Francisco"},
        {"name": "Charlie",
         "event_title": "AI Summit",
         "event_date": None,
         "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees)
