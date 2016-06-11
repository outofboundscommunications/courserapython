
'''
import xml.etree.ElementTree as ET


#data = '''
#<person>
#    <name>Chuck</name>
#    <phone type="intl">+1 734 303 4456</phone>
#    <email hide="yes"/>
#</person>'''

data = '''
<commentinfo>
    <note>This file contains the sample data for testing</note>
<comments>
    <comment>
        <name>Romina</name>
        <count>97</count>
    </comment>
    <comment>
        <name>Laurie</name>
        <count>97</count>
    </comment>
    <comment>
        <name>Bayli</name>
        <count>90</count>
    </comment>
</comments>
</commentinfo>

'''

'''
tree = ET.fromstring(data)

print 'Name:',tree.find('name').text
print 'Attr:',tree.find('email').get('hide')
print 'Name:',tree.find('phone').text

'''
'''
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')
print 'comment count:', len(lst)

mySum = 0
for item in lst:
    print 'Name:',item.find('name').text
    print 'Count:',item.find('count').text
    mySum = mySum + int(item.find('count').text)

print 'the sum is: ', mySum

'''

import json

input = '''
{ "id" : "001",
  "x" : "2",
  "name" : "Chuck"
} '''
    

info = json.loads(input)
print 'User count:', len(info)
print info

print 'Name', info['name']
print 'Id', info['id']
print 'Attribute', info['x']

