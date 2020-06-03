#!/usr/bin/python3
""" This module contains a single function.
"""



def from_json_string(my_str):
    """
    function that returns an object
    """
    import json
    return json.loads(my_str)
