#!/usr/bin/python

import MySQLdb as sql
from tabulate import tabulate

def connect(l):
    try:
        db = sql.connect(l[0], l[1], l[2], l[3])
        cursor = db.cursor()
        while(True):
            query = raw_input('Query (e for exit): ')
            if(query == 'e'):
                break
            cursor.execute(query)
            columns = cursor.description
            rows = []
            header = []
            for i in columns:
                header.append(i[0])
            for row in cursor.fetchall():
                rows.append(row)
            print tabulate(rows, header)
    except sql.Error, e:
        print('Error: %d %s' % (e.args[0], e.args[1]))

def main():
    while(True):
        s = raw_input('Connect to database (q to quit) - host username password database: ')
        if(s == 'q'):
            break
        l = s.split()
        connect(l)

if(__name__ == '__main__'):
    main()

