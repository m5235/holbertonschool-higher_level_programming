#!/usr/bin/python3
"""
module function.
"""


def read_lines(filename="", nb_lines=0):
    """Reads nb lines from file and prints it to stdout."""

    with open(filename, mode='r', encoding='UTF8') as file:
        if nb_lines <= 0:
            for line in file:
                print(line, end='')
        else:
            for i in range(nb_lines):
                print(file.readline(), end='')
