#!/usr/bin/python

def fibonacci(n):
    fnminus2 = 0
    fnminus1 = 1
    print 'F0 = ' + str(fnminus2)
    if(n == 1):
        return
    print 'F1 = ' + str(fnminus1)
    count = 2
    while(count < n):
        fn = fnminus1 + fnminus2
        fnminus2 = fnminus1
        fnminus1 = fn
        print 'F' + str(count) + ' = ' + str(fn)
        count += 1
    return

def main():
    while(True):
        s = raw_input('Enter the number of fibonacci numbers (q for quit): ')
        if(s == 'q'):
            break
        try:
            n = int(s)
            try:
                assert n > 0
            except AssertionError:
                print 'Enter a number > 0'
                return
            fibonacci(n)
        except (ValueError, SyntaxError):
            print('Please enter a valid integer.')

if(__name__ == '__main__'):
    main()
