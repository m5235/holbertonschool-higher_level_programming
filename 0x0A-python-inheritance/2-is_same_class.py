#!/usr/bin/python3
""" Function is_same_class"""


def is_same_class(obj, a_class):
    """function of object exactly an instance of the spacified class"""
    return type(obj) is a_class
