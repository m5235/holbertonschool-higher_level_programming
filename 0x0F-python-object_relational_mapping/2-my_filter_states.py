#!/usr/bin/python3
"""
task two
"""

if __name__ == "__main__":
    import MySQLdb as mysql
    from sys import argv as args

    mysql_username = args[1]
    mysql_password = args[2]
    db_name = args[3]
    argument = args[4]

    database = mysql.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=db_name)

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}%';\
                    ORDER BY state.id".format(argument))

    result = cursor.fetchall()
    for rows in result:
            print(rows)
