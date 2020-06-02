#!/usr/bin/pyhon3

""" function some classes"""


def inherits_from(obj, a_class):

    """ function that returns True if the object
    is an instance of a class"""
    return False if type(obj) is a_class else isinstance(obj, a_class)
