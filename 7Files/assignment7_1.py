'''
7.1 Write a program that: 
1- prompts for a file name
2 - then opens that file and 
3- reads through the file, and 
4 - print the contents of the file in upper case. 

Use the file words.txt to produce the output below.
You can download the sample data at http://www.pythonlearn.com/code/words.txt


'''
#prompt for file name
inpfile = raw_input("Enter file name:")

myCounter = 0

#open that file
fhand = open(inpfile,'r')
for line in fhand:
    line = line.rstrip()
    print(line.upper())
    
    