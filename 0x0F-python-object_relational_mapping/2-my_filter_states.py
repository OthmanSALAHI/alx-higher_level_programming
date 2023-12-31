#!/usr/bin/python3
"""the state with name"""


from sys import argv
import MySQLdb


def connect_db():
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS like '{}'".format(argv[4]))
    states = cursor.fetchall()
    for state in states:
        print(state)
    db.close()


if __name__ == "__main__":
    connect_db()
