

'''
Exercise 10.1 Revise a previous program as follows: 
1. Read and parse the From lines and pull out the addresses from the line. 
2. Count the number of messages from each person using a dictionary.
3. After all the data has been read, print the person with the most commits by creating
    a list of (count, email) tuples from the dictionary. 
    Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195

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
    emailtext = words[1]
    #2. Count the number of messages from each person using a dictionary.
    d[emailtext] = d.get(emailtext,0)+1   

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
