#!/usr/bin/python3
"""
task0
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    database = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3]
            )
    cursor = database.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for i in rows:
        print(i)

    cursor.close()
    database.close()
