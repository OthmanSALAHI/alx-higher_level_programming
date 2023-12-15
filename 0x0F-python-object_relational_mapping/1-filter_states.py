#!/usr/bin/python3
"""select the N states"""


from sys import argv
import MySQLdb

if __name__ == '__main__':
    data_base = MySQLdb.connect(user=argv[1], passwd=argv[2],
                                db=argv[3], port=3306)
    cur = data_base.cursor()
    cur.execute("SELECT * FROM states WHERE `name` LIKE 'N%';")
    states = cur.fetchall()
    for state in states:
        print(state)
    db.close()
