

'''
read through the list of negatives and campaigns and store in dictionary

'''

import string 

fhand = "negativesList.csv"

f2hand = "Report.csv"
    
negatives = dict()

acctnegatives = dict()


for line in fhand:
    line = line.rstrip()
    #split the line, at each comma, into a list 
    words = line.split(',')
    #if line empty, skip
    if len(words)==0:
        continue
    #if header, skip
    if words[0] =='Campaign':
        continue
    #parse out the negative keyword text (its the third element in the list)
    negtext = words[2]
    print negtext, matchtype
    matchtype = words[3]
    if negtext not in negatives:
        negatives[negtext] = matchtype
#print counts

'''
for key in negatives:
    print key, negatives[key]

'''