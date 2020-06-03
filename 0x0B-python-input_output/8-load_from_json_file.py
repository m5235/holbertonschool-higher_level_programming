#!/usr/bin/python3
"""
module  function.
"""


def load_from_json_file(filename):
    """
    reates an Object from a “JSON file”:
    """
    import json
    with open(filename, mode='r') as file:
        file_ = file.read()

    return json.loads(file_)
