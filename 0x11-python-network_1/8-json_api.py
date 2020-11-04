#!/usr/bin/python3
""" task 9
"""
if __name__ == "__main__":

import requests
import sys

    url = "http://0.0.0.0:5000/search_user"
 # take argument

    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    response = requests.post(url, data=data)

    try:
        d = response.json()
        if not d:
            print("No result")
        else:
            print("[{}] {}".format(d.get("id"), d.get("name")))
    except ValueError:
        print("Not a valid JSON")