__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.

'''
read through the messy google feed and store in dictionary
using item id as key and rest of comma separated fields as values

'''

import urllib
import re


link = "https://wakeeffects.com/?woocommerce_gpf=bing"
try:
    fname = urllib.urlopen(link)
except:
    print 'the url could not be opened:', fname
    exit()

count = 0
labels =[]
fhand = fname.readlines()
for line in fhand:
    x = re.findall('[wW]akeboard.+',line)
    if len(x) > 0:
        labels.append(line)
        #print 'hit'
        #print line
print 'the number of hits found is: ', len(labels)

print labels