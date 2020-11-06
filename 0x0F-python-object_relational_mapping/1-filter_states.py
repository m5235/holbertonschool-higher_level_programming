#!/usr/bin/python3
"""
task 1
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    database = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
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
    database.close()
