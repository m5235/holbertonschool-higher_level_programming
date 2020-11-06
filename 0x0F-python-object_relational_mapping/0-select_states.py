#!/usr/bin/python3

"""
task 0
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # connect to Mysql server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    num_rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    for i in range(num_rows):
        print(row)
    cur.close()
    con.close()cat
