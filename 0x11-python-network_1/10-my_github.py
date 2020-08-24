#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
import requests
import sys


if __name__ == "__main__":
    res = get("https://api.github.com/user", auth=(argv[1], argv[2])).json()
    try:
        print(res['id'])
    except:
        print('None')
