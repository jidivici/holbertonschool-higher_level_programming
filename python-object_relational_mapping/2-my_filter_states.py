#!/usr/bin/python3
"""Displays all values in states where name matches the argument"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states "
                   "WHERE name = '{}' "
                   "ORDER BY id ASC").format(sys.argv[4],)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
