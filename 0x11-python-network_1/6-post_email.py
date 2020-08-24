#!/usr/bin/python3
"""
send post request using requests module.
"""
import requests
from sys import argv
if __name__ == "__main__":
    url = sys.argv[1]
    myobj = {"email": sys.argv[2]}
    print(requests.post(url, data=myobj).text)
