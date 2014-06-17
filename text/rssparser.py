#!/usr/bin/python

import xml.etree.ElementTree as ET
import urllib2

def posts(tree):
    root = tree.find('channel')
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
        if(not(item.find('author') == None)):
            print 'author:', item.find('author').text
        if(not(item.find('enclosure') == None)):
            print 'enclosure:', item.find('enclosure').get('url')
        if(not(item.find('pubDate') == None)):
            print 'pubDate:', item.find('pubDate').text
        print ''
        count += 1


def main():
    while(True):
        filename = raw_input('Enter xml file name (q to quit): ')
        if(filename == 'q'):
            break
        try:
            tree = ET.parse(filename)
            posts(tree.getroot())
        except:
            try:
                filexml = urllib2.urlopen(filename)
                filexml_string = filexml.read()
                tree = ET.fromstring(filexml_string)
                posts(tree)
            except:
                print 'File is invalid or does not exist'

if(__name__ == '__main__'):
    main()
