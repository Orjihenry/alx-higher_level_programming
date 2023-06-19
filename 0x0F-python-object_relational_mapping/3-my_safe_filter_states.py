#!/usr/bin/python3
"""
Displays all values in the states
where `name` matches the argument
from the db `hbtn_0e_0_usa`.

This script is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Get the states from the db
    when connection is established
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
