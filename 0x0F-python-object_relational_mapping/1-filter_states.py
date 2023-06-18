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
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    states = db_cursor.fetchall()

    for state in states:
        print(state)
