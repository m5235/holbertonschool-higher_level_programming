#!/usr/bin/python3
"""  module  function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON r
    """

    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
