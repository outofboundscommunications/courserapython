__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.

'''
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number 
of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person 
who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of 
the number of times they appear in the file. 
After the dictionary is produced, the program reads through the 
dictionary using a maximum loop to find the most prolific committer.


largest = None
print 'Before:', largest
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print 'Loop:', itervar, largest
print 'Largest:', largest
'''
import string

#define dictionary
d = dict()
#define largest variable
largest = None
prolific = None

name = raw_input("Enter file:")
if len(name) < 1 : 
    name = "mbox-short.txt"
handle = open(name)

#read each line in words.txt
for line in handle:
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
for key in sorted(d):
    if largest is None or d[key] > largest :
        largest = d[key]
        prolific = key
print prolific,largest
        
