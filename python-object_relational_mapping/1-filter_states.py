#!/usr/bin/python3
"""Lists all states with a name starting with N from
    the database hbtn_0e_0_usa.

Logic:
- Connect to MySQL using MySQLdb with credentials from argv
- Use a WHERE clause with LIKE 'N%' to filter server-side
"""
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
                   "WHERE name LIKE BINARY 'N%' "
                   "ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
