#!/bin/bash
# Sends a request to a URL passed as an argument, displays the response status
curl -s -o /dev/null -w "%{http_code}" "$1"
