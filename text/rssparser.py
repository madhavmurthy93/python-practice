#!/usr/bin/python

import xml.etree.ElementTree as ET

def posts(tree):
    root = tree.getroot().find('channel')
    print 'title:', root.find('title').text
    print 'link:', root.find('link').text
    print 'description:', root.find('description').text
    print ''
    print 'stories:'
    count = 1
    for item in root.findall('item'):
        print 'story', str(count)
        if(not((item.find('title')) == None)):
            print 'title:', item.find('title').text
        if(not((item.find('link')) == None)):
            print 'link:', item.find('link').text
        if(not((item.find('description')) == None)):
            print 'description:', item.find('description').text
        print ''
        count += 1


def main():
    while(True):
        filename = raw_input('Enter xml file name (q to quit): ')
        if(filename == 'q'):
            break
        tree = ET.parse(filename)
        posts(tree)

if(__name__ == '__main__'):
    main()
