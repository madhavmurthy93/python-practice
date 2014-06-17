#!/usr/bin/python

def is_palindrome(string):
    l = list(string)
    pal = True
    for i in range(int(len(l) / 2)):
        if(not(l[i] == l[len(l) - 1 - i])):
            pal = False
    return pal

def main():
    while(True):
        s = raw_input('Enter a string (q to quit): ')
        if(s == 'q'):
            break
        print 'Palindrome:', is_palindrome(s)

if(__name__ == '__main__'):
    main()

