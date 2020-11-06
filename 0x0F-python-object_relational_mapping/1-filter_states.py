#!/usr/bin/python3

"""
task 1
"""
import sys
import MySQLdb

if __name__ == "__main__":

    # connect to Mysql server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user_name=sys.argv[1],
            Mypasswd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
            )
    cursor = db.cursor()
    cursor.execute(
            "SELECT id, name FROM states WHERE name LIKE BINARY 'N%'\
            ORDER BY id ASC"
            )
    query = cursor.fetchall()
    for row in query:
        print(row)
    cursor.close()
    db.close()
