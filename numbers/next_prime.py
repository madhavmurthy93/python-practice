#!/usr/bin/python

number = 2

def find_prime():
    global number
    while(True):
        is_prime = True
        factor = 2
        limit = int(number / 2)
        while(factor <= limit):
            if(number % factor == 0):
                is_prime = False
                break
            else:
                factor += 1
        number += 1
        if(is_prime):
            return (number - 1)
    return 0

def main():
    while(True):
        s = raw_input('Find next prime (y/n): ')
        if(s == 'n'):
            break
        prime = find_prime()
        print str(prime)

if(__name__ == '__main__'):
    main()
