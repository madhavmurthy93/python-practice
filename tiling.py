#!/usr/bin/python

def find_cost(width, height, cost):
    return (width * height * cost)

def main():
    while(True):
        try:
            width = int(raw_input('Enter width of floor: '))
            height = int(raw_input('Enter height of floor: '))
            cost = int(raw_input('Enter cost per square unit: '))
            total_cost = find_cost(width, height, cost)
            print 'Total cost is: ' + str(total_cost)
            if(raw_input('Quit (y/n): ') == 'y'):
                break
        except (ValueError, SyntaxError):
            print 'Enter valid number'

if(__name__ == '__main__'):
    main()

