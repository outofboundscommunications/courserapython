__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.

'''
read in csv file of links of competitors
for each line:
    check to see if sending domain exists dictionary
    if exists:
        continue
    add sending domain to domain list
'''
import string
import csv

#define dictionary
d = dict()
#define largest variable
largest = None
prolific = None

name = raw_input("Enter file:")
if len(name) < 1 : 
    name = "combined.csv"
handle = open(name)

#read each line in csv file
for line in handle:
    if line.startswith('SendingDomain'):
        continue
    line = line.rstrip()
    #split the line into fragments so we can find sending domain and target domain
    words = line.split(',')
    if len(words) == 0 : 
        continue
    #parse out the sending domain portion (1st column or '0' element)
    sendingDomain = words[0]
    #print sendingDomain
    #parse out the target domain portion (11th column or '10th element)
    targetDomain = words[10]
    #skip africastyles.com domain data, lots of spammy .ru links
    if 'africastyles.com' in targetDomain:
        continue
    #print targetDomain
    #if sendingDomain no in dictionary then add as key and add targetDomain as value
    if sendingDomain not in d:
        d[sendingDomain] = targetDomain  

#open file for writing out dictionary
'''
fout = open('awaleResults.txt','w')
for key in sorted(d):
    #print key,d[key]
    fout.write(key,d[key])
'''
with open('awaleResults.csv','wb') as f:
    #w=csv.DictWriter(f,d.keys())
    w=csv.writer(f)
    w.writerows(d.items())

