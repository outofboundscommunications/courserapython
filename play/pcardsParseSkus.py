__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
'''
we want to parse out the product sku numbers from the urls
the file contains category pages, product pages and static pages
the product urls have the following format:
http://postycards.com/catalog/product/Fireworks_Chinese_New_Year_A6057U
http://postycards.com/catalog/product/Patriotic_Ornament_X549S

So you want to look for a string that contains "product"
then parse out the substring that is the after the final "_" (_X549S ---> X549X)

1. read in the postycards cms export file (csv)
2. for each line:
    look for the 'product' string
    if you find:
        look for the final "_" and parse out the string following
        store the string in a list
    if you don't find:
        continue




'''
import string 
import re
import csv

##### process/open/check file ##################
#
fname = raw_input('Enter the file name: ')
if len(fname)==0:
    fname = "postycards_internal_html.csv"
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

### end of file processing #####################

#define empty sku list
activeSkus = []
### read in each line of file and use regex to look for a string that looks like a product  ###########
for line in fhand:
    #strip end of line character
    line = line.rstrip()
    #example string: http://postycards.com/catalog/product/Patriotic_Ornament_X549S
    if re.search('product',line):
        mysku = re.findall('_.*?',line)  
        activeSkus.append(mysku)

for sku in activeSkus:
    print sku
    
fout = open('postyskus.txt','w')

str1 = ',\n'.join(str(v) for v in activeSkus)

fout.write(str1)
    
fout.close()
   
