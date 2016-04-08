__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.

'''
Exercise 9.3 Write a program to read through a mail log, build a histogram using
a dictionary to count how many messages have come from each email address,
and print the dictionary.

example output:

Enter file name: mbox-short.txt

{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}


'''

import string

#define dictionary
d = dict()

#process/open/check file
fname = raw_input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"
try :
    fhand=open(fname)
except :
    print 'Cannot open file:' , fname , '.' , '...please try, again.'
    exit()

#read each line of opened file and process
for line in fhand:
    line = line.rstrip()
    #split the line into words
    words = line.split()
    if len(words) == 0 : 
        continue
    if words[0] != 'From' : 
        continue
    #parse out the email address portion
    emailtext = words[1]
    #use the .get() idiom as more concise logic than the if statement below
    d[emailtext] = d.get(emailtext,0)+1   

#print out dictionary
#for key in sorted(d):
for key in d:
    print key,d[key]
    
        