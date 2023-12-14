#!/usr/bin/python3

from sys import argv
import MySQLdb

def connect_sql():
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                        db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute(f"SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id;")
    result = cursor.fetchall()
    for i in result:
        print(i)
    db.close()

if __name__ == "__main__":
    connect_sql()