__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.

'''
read through a postycards html page and parse out the category names and their ids

'''

import string 
import re
import csv

##### process/open/check file ##################
#
fname = raw_input('Enter the file name: ')
if len(fname)==0:
    fname = "postycards_html.txt"
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

### end of file processing #####################

categories = []
### read in each line of file and use regex to look for a string that looks like a subcategory  ###########
for line in fhand:
    #strip end of line character
    line = line.rstrip()
    #use regex to add each number found to list
    lst = re.findall('subcategory_[0-9].*title=.*?>' , line)   
    #if row/list length is >0, then we have a match and need to store
    if len(lst) >0:
        categories.append(lst)
    
#print counts
print 'the number of categories is: ', len(categories)

fout = open('postycats.txt','w')

#str1 = "".join(categories)
#str1 = "".join(str(x) for x in categories)
str1 = ',\n'.join(str(v) for v in categories)
for cat in categories:
    print cat

fout.write(str1)
    
fout.close()
