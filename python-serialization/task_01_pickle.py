#!/usr/bin/env python3
"""Module for custom object serialization using pickle."""
import pickle


class CustomObject:
    """A custom class that supports pickle-based serialization."""

    def __init__(self, name="", age=0, is_student=True):
        """Initialize a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes to standard output."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object and save it to a file using pickle.

        Args:
            filename (str): The path of the file to write the object to.
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return a CustomObject from a pickle file.

        Args:
            filename (str): The path of the file to read the object from.

        Returns:
            CustomObject: The deserialized object, or None on failure.
        """
        with open(filename, "rb") as f:
            return pickle.load(f)
