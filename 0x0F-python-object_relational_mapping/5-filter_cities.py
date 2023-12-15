#!/usr/bin/python3
"""show states"""


from sys import argv
import MySQLdb


def connect_sql():
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name \
    FROM cities JOIN states ON cities.state_id = states.id WHERE\
    states.name like '{}';".format(argv[4]))
    result = cursor.fetchall()
    print(", ".join([i[0] for i in result]))


if __name__ == "__main__":
    connect_sql()
