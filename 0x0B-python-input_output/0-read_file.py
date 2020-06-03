#!/usr/bin/python3
"""
module file
"""


def read_file(filename=""):
    """
    function that reads
    a text file and prints it to stdout
    """
    with open(filename, mode='r', encoding='UTF8') as file:
        for line in file:
            print(line, end="")
