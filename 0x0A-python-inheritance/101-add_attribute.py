#!/usr/bin/python3
"""can"""


def add_attribute(obj, atr, value):
    """
    adding a new attribute to an object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, value)