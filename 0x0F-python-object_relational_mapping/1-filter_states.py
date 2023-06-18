#!/usr/bin/python3
"""
Script that lists all states in db = hbtn_0e_0_usa.
Only lists states starting with upper N
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':   # Run code only when executed directly.
    """
    Get the states from the database
    when connection has been established.
    """
    # Establish connection
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()   # Cursor object to execute queries.

    db_cursor.execute("SELECT * FROM states WHERE name LIKE N% \
        ORDER BY states.id ASC")   # Filters only states starting with upper N

    states = db_cursor.fetchall()  # Checks whole data and displays only result

    for state in states:
        print(state)
