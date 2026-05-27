#!/usr/bin/env python3
"""Module for custom object serialization using pickle."""
import pickle


class CustomObject:
    """A custom class that supports pickle-based serialization."""

    def __init__(self, name="", age=0, is_student=True):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes to standard output."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object and save it to a file using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return a CustomObject from a pickle file."""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            return None
        return None
