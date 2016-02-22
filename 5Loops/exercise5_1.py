__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
'''
1. read a list of numbers until done' is entered
2.then print out total, count and average
3.if user enters anything besides a number, print error message
and skip to next entry


'''
#initialize variables
tot = 0
cnt = 0
avg = 0

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
    #if input not a number
    if is_number(inpstr) is False:
        #if they entered done, then break
        if inpstr == 'done':
            print tot,cnt,avg
            break
        #otherwise, return to start of loop and ask again for input
        else:
            continue
    elif is_number(inpstr):
        tot +=float(inpstr)
        cnt +=1
        avg =tot/cnt 