#!/usr/bin/python3
""" function same class  """


class BaseGeometry:

    """ BaseGeometry class """


def area(self):
    """ def calculate area"""
raise Exception("area() is not implemented")


def integer_validator(self, name, value):
    """  validate value      """
    if type(value) is not int:
          raise TypeError("{} must be an integer".format(name))
        if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))