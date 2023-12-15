#!/usr/bin/python3
"""select the N states"""


from sys import argv
import MySQLdb

if __name__ == '__main__':
    data_base = MySQLdb.connect(user=argv[1], passwd=argv[2],
                                db=argv[3], port=3306)
    cur = data_base.cursor()
    cur.execute("SELECT * FROM states WHERE  CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS LIKE 'N%';")
    states = cur.fetchall()
    for state in states:
        print(state)
    data_base.close()
