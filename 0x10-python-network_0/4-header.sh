#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the UR
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
