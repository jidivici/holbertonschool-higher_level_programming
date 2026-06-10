#!/usr/bin/python3
"""Displays all values in states where name matches the argument"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    name = sys.argv[4].replace("'", "\\'")
    query = ("SELECT * FROM states "
             "WHERE name = '{}' "
             "ORDER BY id ASC").format(name)
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
