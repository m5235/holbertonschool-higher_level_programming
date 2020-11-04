#!/usr/bin/python3
""" task 10
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    response = requests.get(url, auth=auth)
    try:
        print(response.json().get("id"))
    except :
        print("Not a valid JSON")