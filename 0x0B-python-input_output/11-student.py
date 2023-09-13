#!/usr/bin/python3
"""
Contains the class "Student"
"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the student instance.

        Args:
            attrs (list, optional): The list of attribute names to retrieve.
                If None, all attributes are retrieved. Defaults to None.
        """
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if type(attr) is str and hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """Replaces all attributes of the student instance with the values
           from the provided dictionary.

        Args:
            json (dict): The dictionary containing the attribute
            names and values.
        """
        for attr, value in json.items():
            setattr(self, attr, value)
