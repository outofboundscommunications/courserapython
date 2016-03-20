__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
'''
8.4 Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words 
using the split() method. 
The program should build a list of words. For each word on each line check to see if 
the word is already in the list and if not append it to the list. 
When the program completes, sort and print the 
resulting words in alphabetical order.

You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
print line.rstrip()


'''
#assign file name to variable
fname = 'romeo.txt'
#define wordlist
wordlist =[]
try:
    #open the file romeo.txt
    fhand = open(fname)
    #For each line, split the line into a list of words 
    for line in fhand:
        #strip end of line character
        line = line.rstrip()
        #convert all characters to lower case
        #line = line.lower()
        #split line into words
        words = line.split()
        for word in words:
            if word in wordlist:
                #print 'the word: ', word, ' is already in the list.'
                continue
            else:
                wordlist.append(word) 
                #print 'the word: ', word, ' was appended to the list.'
except:
    print 'File cannot be opened:', fname
    exit()

'''
When the program completes, sort and print the 
resulting words in alphabetical order.
'''   

#sort the list
wordlist.sort()

#print out sorted list
print wordlist

'''
for element in wordlist:
        print element
'''