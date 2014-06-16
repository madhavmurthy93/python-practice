#!usr/bin/python

import sys

def find_pi(limit):
    return 3.14

def main():
    valid = False
    while(not(valid)):
        try:
            limit = int(input('Enter the number of digits of pi: '))
            while(limit <= 0 or limit >= 200):
                print 'Please enter a number > 0 & < 200: '
                limit = int(input('Enter the number of digts of pi: '))
            valid = True
            pi = find_pi(limit)
        except (ValueError, NameError, SyntaxError):
            print 'Please enter a valid integer.'
    print 'The value of pi to the ' + str(limit) + 'th digit is: ' + str(pi)

if( __name__ == '__main__'):
    main()
