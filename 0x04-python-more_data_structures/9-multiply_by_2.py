#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = list(a_dictionary.keys())
    new_dictionary = {}
    for x in keys:
        new_dictionary[x] = a_dictionary[x] * 2
    return new_dictionary
