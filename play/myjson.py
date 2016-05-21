__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#

import urllib
import json

url = 'https://trello.com/b/j9a24Wka.json'

while True:
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    print json.dumps(js, indent=4)