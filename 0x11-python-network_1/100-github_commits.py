#!/usr/bin/python3
"""
task 11
"""
if __name__ == '__main__':

    import requests
    import sys
 url = 'https://api.github.com/repos/{}/{}/commits'
    r = requests.get(url.format(sys.argv[2], sys.argv[1]))
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
