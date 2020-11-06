#!/usr/bin/python3
"""
task0
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for element in rows:
        print(element)

    cursor.close()
    db.close()
