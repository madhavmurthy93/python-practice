#!/usr/bin/python

import math

def prime_factors(n):
    try:
        assert n > 1
    except AssertionError:
        print 'Enter an integer > 1'
        return
    factors = []
    factor = 2
    limit = int(n / 2);
    while(factor <= limit):
        if(n % factor == 0):
            factors.append(factor)
            n = n / factor
        else:
            factor += 1
    if(len(factors) == 0):
        print str(n) + ' is a prime number'
    else:
        print str(factors).strip('[]')

def main():
    while(True):
        s = raw_input('Find the prime factors of (q for quit): ')
        if(s == 'q'):
            break
        try:
            n = int(s)
            prime_factors(n)
        except (ValueError, SyntaxError):
            print 'Enter a valid integer'

if(__name__ == '__main__'):
    main()
