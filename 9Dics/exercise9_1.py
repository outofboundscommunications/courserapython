__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
'''
write a program that reads the words in words.txt and stores them as keys in a dic.
doesnt matter what values are.
then you can use the in operator as a fast way to check whether a string is in the dictionary.

'''
#define dictionary
d = dict()

#open file
fname = raw_input("Enter file name: ")
if len(fname) < 1 : 
    fname = "words.txt"
fhand = open(fname)
#read each line in words.txt
for line in fhand:
    line = line.rstrip()
    #split the line into words
    words = line.split()
    for word in words:
            #use the .get() idiom as more concise logic than the if statement below
            d[word] = d.get(word,0)+1
            '''
            if word not in d:
                d[word] = 1
            else:
                d[word] = d[word]+1
            '''
for key in sorted(d):
    print key, d[key]

#then you can use the in operator as a fast way to check whether a string is in the dictionary.
print 'this' in d
print 'the' in d