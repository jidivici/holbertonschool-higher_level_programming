#!/usr/bin/python3
"""Displays all values in states where name matches the argument — SQL injection safe.

Logic:
- Instead of interpolating user input into the query string (task 2),
  we pass it as a separate parameter tuple to cursor.execute().
- MySQLdb escapes the value before sending it to the server, so special
  characters like quotes, semicolons, etc. are treated as literal data,
  never as SQL syntax.
- The placeholder in the query is %s (MySQLdb convention), NOT a Python
  format specifier — the driver handles the substitution at the protocol level.

Comparison:
  UNSAFE:  cursor.execute("... WHERE name = '{}'".format(user_input))
  SAFE:    cursor.execute("... WHERE name = %s", (user_input,))
"""
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
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
