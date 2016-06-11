'''
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. 
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the 
comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the 
other is the actual data you need to process for the assignment.

Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_232819.json (Sum ends with 0)
You do not need to save these files to your folder since your program will read the data directly from the URL. 
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

Data Format
The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
The closest sample code that shows how to parse JSON and extract a list is json2.py. 
You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.

Sample Execution

$ python solution.py 
Enter location: http://python-data.dr-chuck.net/comments_42.json
Retrieving http://python-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...
Turning in the Assignment

Enter the sum from the actual data and your Python code below:
Sum: 
 (ends with 0) Submit Assignment
Python code:


'''

import json
import urllib


input = '''
{
  "note":"This file contains the sample data for testing",
  "comments":[
    {
      "name":"Romina",
      "count":97
    },
    {
      "name":"Laurie",
      "count":97
    },
        {
      "name":"Inika",
      "count":2
    }
  ]
}

'''
mySum = 0
myCounter = 0

while True:
    url = raw_input('Enter location: ')
    if len(url) < 1 : 
        break
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    #print data
    info = json.loads(str(data))

    for item in info["comments"]:
        #print item["name"]
        #print item["count"]
        mySum = mySum +int(item["count"])
        myCounter = myCounter+1

print "count: " ,myCounter
print "sum: ", mySum
