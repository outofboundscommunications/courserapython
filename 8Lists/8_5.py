__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
'''

1. Open the file mbox-short.txt and read it line by line. 
2. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
3. you will parse the From line using split() and print out the second word in the line 
(i.e. the entire address of the person who sent the message). 
4. Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.tx

fname = raw_input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
print "There were", count, "lines in the file with From as the first word"

'''
fname = raw_input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"
fhand = open(fname)
count = 0
#read it line by line. 
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 : 
        continue
    if words[0] != 'From' : 
        continue
    count +=1
    #parse out the email address portion
    emailtext = words[1]
    print emailtext

print 'There were ', count, ' lines in the file with From as the first word.'
 