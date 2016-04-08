__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.

'''
Exercise 9.2 Write a program that categorizes each mail message by which day
of the week the commit was done. To do this look for lines that start with From
then look for the third word and keep a running count of each of the days of the
week. At the end of the program print out the contents of your dictionary (order
does not matter)

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}

'''

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

#read each line in words.txt
for line in fhand:
    line = line.rstrip()
    #split the line into words
    words = line.split()
    if len(words) == 0 : 
        continue
    if words[0] != 'From' :  
        continue
    #parse out the day of week portion
    print 'we have a hit. the line is: ',words[2]
    dayofweektext = words[2]
    #if key present, increment counter, if not, set counter to 1
    d[dayofweektext] = d.get(dayofweektext,0)+1 

#print out dict
print d