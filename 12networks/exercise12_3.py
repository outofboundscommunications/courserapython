

'''
Following Links in Python

In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. 
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor 
tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link 
and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. 

One is a sample file where we give you the name for your testing and 
the other is the actual data you need to process for the assignment

http://www.py4inf.com/book.htm

Sample problem: 

Start at http://python-data.dr-chuck.net/known_by_Fikret.html 
Find the link at position 3 (the first name is 1). Follow that link. 
Repeat this process 4 times. 
The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
Last name in sequence: Anayah

Actual problem: 

Start at: http://python-data.dr-chuck.net/known_by_Mercedez.html 
Find the link at position 18 (the first name is 1). Follow that link. 
Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: G

Strategy

The web pages tweak the height between the links and hide the page after a few seconds to make 
it difficult for you to do the assignment without writing a Python program. 
But frankly with a little effort and patience you can overcome these attempts to make it a little 
harder to complete the assignment without writing a Python program. 
But that is not the point. The point is to write a clever Python program to solve the program.

Sample execution

Here is a sample execution of a solution:

$ python solution.py 
Enter URL: http://python-data.dr-chuck.net/known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving: http://python-data.dr-chuck.net/known_by_Fikret.html
Retrieving: http://python-data.dr-chuck.net/known_by_Montgomery.html
Retrieving: http://python-data.dr-chuck.net/known_by_Mhairade.html
Retrieving: http://python-data.dr-chuck.net/known_by_Butchi.html
Retrieving: http://python-data.dr-chuck.net/known_by_Anayah.html
The answer to the assignment for this execution is "Anayah".

Turning in the Assignment

Enter the last name retrieved and your Python code below:
Name: (name starts with G) 


Submit Python code:

'''

import urllib
from BeautifulSoup import *

urlToFetch = raw_input('Enter URL: ')
counter= int(raw_input('Enter count:'))
targetPosition =int(raw_input('Enter position:'))

#define list to store links found
#add the first url (fikret)
linksFound =['fikret']

#define function for fetching
def fetchLinks(targetPosition,urlToFetch):
    currentPosition=0
    html = urllib.urlopen(urlToFetch).read()
    soup = BeautifulSoup(html)
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        theLink = tag.get('href', None)
        print 'Retrieving:',theLink
        currentPosition = currentPosition + 1
        if currentPosition == targetPosition:
            #print 'the link at your target position of: ', targetPosition,' is: ', theLink
            #print 'TAG:',tag
            #print 'URL:',tag.get('href', None)
            #print 'Content:',tag.contents[0]
            linkToFollow = theLink
            anchorText = tag.contents[0]
            #add this link to the list
            linksFound.append(anchorText)
            print 'the new link to follow is: ', linkToFollow
            print 'the anchor text is: ', anchorText
            return urlToFetch
     
n=0
while n<counter:
    fetchLinks(targetPosition,urlToFetch)
    n=n+1
      
for item in linksFound:
    print item