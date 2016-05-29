__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
'''
1. read in the google merchant feed file (text file with line breaks)
2. for each line:
    lookup the text after the dash in the 'id' field
    match to one of the pricing codes in the code dictionary
    if it matches one of the keys, the pull the value from that key (the price) and insert as the price value for that product record 



notes from client about pricing:

Since our minimum order is 50, we want to use the 50 quantity price. Then you can use a standard shipping charge of $8.50. 
If I give you a price for each price code, could you update the spreadsheet? The price code is after the dash in the item ID.
4W: $85
V: $56
W: $43.50
X: $37
Y: $33
Z: $27
ZZ: $24.50
4A: $89.50
4B: $60
AAA: $45.50
AA: $40.50
A: $35.50
B: $29.50
BB: $24.50

'''
#define price dictionary
priced = {'4W':'85.00 USD','V':'56.00','W':'43.50'}

prodd = dict()

#open file
fname = raw_input("Enter file name: ")
if len(fname) < 1 : 
    fname = "GoogleDataFeed.txt"
fhand = open(fname)
#read each line text file
for line in fhand:
    line = line.rstrip()
    #split the line into words
    words = line.split(',')
    if len(words) == 0:
        continue
    print words[0]


