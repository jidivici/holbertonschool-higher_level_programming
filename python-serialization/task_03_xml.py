#!/usr/bin/env python3
"""Module for XML serialization and deserialization."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """Deserialize an XML file to a dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}

    for child in root:
        text = child.text
        if text is None:
            value = None
        else:
            try:
                value = int(text)
            except ValueError:
                try:
                    value = float(text)
                except ValueError:
                    value = text
        data[child.tag] = value
    return data
