#!/usr/bin/python3
"""
Contains the add_attribute function
"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it’s possible

    Args:
        obj: any object
        name: a string
        value: any value

    Raises:
        TypeError: if the object can’t have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
