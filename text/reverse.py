#!/usr/bin/python

def reverse(string):
    l = list(string)
    r = list()
    for i in range(len(l)):
        r.append(l.pop())
    return "".join(r)

def main():
    while(True):
        s = raw_input('Enter a string to reverse (q to quit): ')
        if(s == 'q'):
            break
        print 'The reversed string is:', reverse(s)

if(__name__ == '__main__'):
    main()
