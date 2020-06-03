#!/usr/bin/python3
"""
module function
"""


def write_file(filename="", text=""):
    """
writes a string to a text file ()
 and returns the number of characters written
    """
    with open(filename, mode="w", encoding='UTF-8') as file:
        c_num = file.write(text)
    return c_num
