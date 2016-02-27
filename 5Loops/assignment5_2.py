__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.

'''
5.2 
- Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
- Once 'done' is entered, print out the largest and smallest of the numbers. 
- If the user enters anything other than a valid number catch it with a try/except and put out an 
appropriate message and ignore the number. 
- Enter the numbers from the book for problem 5.1 and match the desired output as shown.

largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    print num

print "Maximum", largest

'''

#initialize variables
largestNum = None
smallestNum = None

#function to detect if user entered number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#get user input
while True:
    inpstr = raw_input("Enter a number or 'done' to quit:")
    #case 1: they entered done, we need to exit program
    if inpstr == 'done':
        print 'Maximum is ', largestNum
        print 'Minimum is ', smallestNum
        break
    #case 2: input not a number, prompt user with error message
    elif is_number(inpstr) is False:
        print 'Invalid input'
        continue
    #case 3: valid input so process
    else:
        if largestNum is None or int(inpstr) > largestNum:
            largestNum = int(inpstr)
        if smallestNum is None or int(inpstr) < smallestNum:
            smallestNum = int(inpstr) 