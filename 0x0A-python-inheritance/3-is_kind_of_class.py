#!/usr/bin/python3

""" Function is_same_class"""

def is_kind_of_class(obj, a_class):

    """turns True if the object is an instance of, or if the object is an instance of a class that inherited from"""
    return isinstance(obj, a_class)
