#!/usr/bin/python3
"""the security matters in sql"""


from sys import argv
import MySQLdb


def connect_sql():
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM states WHERE \
    CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS like %s;", (argv[4],))
    result = cursor.fetchall()
    for i in result:
        print(i)
    db.close()


if __name__ == "__main__":
    connect_sql()
