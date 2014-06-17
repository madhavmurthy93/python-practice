#!/usr/bin/python

import MySQLdb as sql

def connect(l):
    try:
        db = sql.connect(l[0], l[1], l[2], l[3])
        while(True):
            query = raw_input('Query (e for exit): ')
            if(query == 'e'):
                break
            db.query(query)
            r = db.use_result()
            for row in r.fetch_row(0):
                print row
    except sql.Error, e:
        print 'Error: %d %s' % (e.args[0], e.args[1])

def main():
    while(True):
        s = raw_input('Connect to database (q to quit) - host username password database: ')
        if(s == 'q'):
            break
        l = s.split()
        connect(l)

if(__name__ == '__main__'):
    main()

