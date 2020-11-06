#!/usr/bin/python3
"""
task0
"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cursor.fetchall()
    for i in query_rows:
        print(i)
    cursor.close()
    db.close()
