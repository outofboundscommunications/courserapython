__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.

import urllib
from BeautifulSoup import *

'''
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print tag.get('href', None)

'''

x = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

print x

html 
