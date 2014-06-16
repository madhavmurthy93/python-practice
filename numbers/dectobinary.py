#!/usr/bin/python

import re

def b2d(val):
    l = list(val)
    count = len(l) - 1
    decimal = 0
    for i in range(len(l)):
        decimal += int(l[count]) * (2 ** i)
        count -= 1
    return decimal

def d2b(decimal):
    if(decimal == 0):
        return '0'
    binary = ''
    while(not(decimal == 0)):
        binary = str(decimal % 2) + binary
        decimal = decimal >> 1
    return binary

def main():
    while(True):
        direc = raw_input('For binary to decimal conversion - 1, For decimal to binary conversion - 2 (q to quit): ')
        if (direc == 'q'):
            break
        else:
            val = raw_input('Convert: ')
            if(direc == '1'):
                if(re.match('^(0|1)+$', val)):
                    decimal = b2d(val)
                    print 'Decimal value is: ' + str(decimal)
                else:
                    print 'Invalid binary value'
            elif(direc == '2'):
                try:
                    decimal = int(val)
                    binary = d2b(decimal)
                    print 'Binary value is: ' + binary
                except (ValueError, SyntaxError):
                    print 'Invalid decimal value'

if(__name__ == '__main__'):
    main()

