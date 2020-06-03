#!/usr/bin/python3
"""
module file
"""


def number_of_lines(filename=""):
    """
    function that
    returns the number of lines of a text file
    """
    number_lines = 0
    with open(filename, mode='r', encoding='UTF8') as file:
        for line in file:
            number_lines += 1

    return number_lines
