#!/usr/bin/python

import sys

def filestats(f):
    lines = 0
    words = 0
    chars = 0
    for line in f:
        lines += 1
        w = line.split()
        words += len(w)
        for word in w:
            chars += len(list(word))
    print 'Lines:', lines
    print 'Words:', words
    print 'Characters:', chars

def main():
    while(True):
        filename = raw_input('Enter name of file (q to quit): ')
        if(filename == 'q'):
            break
        f = open(filename, 'r')
        filestats(f)

if(__name__ == '__main__'):
    main()

