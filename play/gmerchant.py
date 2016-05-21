__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.

'''
read through the messy google feed and store in dictionary
using item id as key and rest of comma separated fields as values

'''

import string 

fname = raw_input('Enter the file name: ')
if len(fname)==0:
    fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()
    
products = []

lineCount = 0

for line in fhand:
    #line = line.translate(None, string.punctuation) 
    line = line.rstrip()
    words = line.split(",")
    if len(words)==0:
        continue
    products.append(line)
    
#print counts
print 'the number of lines is: ', len(products)
ne[n]
    n = n+1