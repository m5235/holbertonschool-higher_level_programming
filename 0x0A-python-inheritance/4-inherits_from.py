#!/usr/bin/pyhon3

"""
 function some classes
 """


def inherits_from(obj, a_class):

    """ function that returns True if the object
    is an instance of a class"""
    if type(obj) is a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
