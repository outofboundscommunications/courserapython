

'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day 
for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting 
the string a second time using a colon.

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
    #You can pull the hour out from the 'From ' line by finding the time and then splitting
    #the string at the colon
    timepos = line.find(":")
    print timepos
    
    hourOfDay = timeOfDayFrag
    colonpos = line.find('0')
    numText = line[zeropos:]
    numFloat = float(numText)
    print myHourMinSecList
    #2. Count the number of messages from each person using a dictionary.
    #parse out the hour element from the list
    myHour = myHourMinSecList[0]
    hourInt = int(myHour)
    d[hourInt] = d.get(hourInt,0)+1   

for k,v in d:
    print k,v
    
'''

# Create a blank list
clist = []

for k in d:
    #append the value, index to the tuple list (clist)
    clist.append((d[k],k))

print "\n"
#print sorted list ###
#sort the list in reverse order and print out the person who has the most commits.
clist.sort(reverse=True)
print 'the sorted list is: ',clist

print "\n"

print 'the sorted list, unpacked, is:'
for v,k in clist:
    print v,k

'''