#!/usr/bin/python3

"""
task 4
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
    cursor.execute('SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states\
            ON cities.state_id=states.id\
            ORDER BY cities.id ASC')
    query = cursor.fetchall()
    for i in query:
        print(i)
    cursor.close()
    database.close()
