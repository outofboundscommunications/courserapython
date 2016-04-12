

'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day 
for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then 
splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

Desired Output
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

04 3                                                                                                                                                                 
06 1                                                                                                                                                                 
07 1                                                                                                                                                                 
09 2                                                                                                                                                                 
10 3                                                                                                                                                                 
11 6                                                                                                                                                                 
14 1                                                                                                                                                                 
15 2                                                                                                                                                                 
16 4                                                                                                                                                                 
17 2                                                                                                                                                                 
18 1                                                                                                                                                                 
19 1 

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
    #if the line doesn't start with 'From' then skip
    if not line.startswith("From ") : 
        continue
    timePos = line.find(":")
    hourPos = timePos-2
    theHour = line[hourPos:timePos]
    #print line,'the hour is: ', theHour
    d[theHour] = d.get(theHour,0)+1   
#print d

#so we can sort the dict, lets convert to list of tuples
t = d.items()
#print t

t.sort()
#print t

'''
for k in d:
    print k,d[k]

'''
#print the final sorted list of time of day and counts using the sorted list of tuples
for k,v in t:
    print k,v
    
