#!/usr/bin/python3

"""
task 3
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    database = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3]
            )
    cursor = database.cursor()
    cursor.execute('SELECT * FROM states\
            WHERE states.name=%s\
            ORDER BY states.id ASC', (sys.argv[4],))
    query = cursor.fetchall()
    for i in query:
        print(i)
    cursor.close()
    database.close()
