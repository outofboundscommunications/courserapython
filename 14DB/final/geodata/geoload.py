import urllib
import sqlite3
import json
import time
import ssl

# If you are in China use this URL:
# serviceurl = "http://maps.google.cn/maps/api/geocode/json?"
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

# Deal with SSL certificate anomalies Python > 2.7
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
scontext = None

# create & connect to db
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# create table
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# open up the text file with all student's locations recorded as strings
fh = open("where.data")
count = 0
for line in fh:
    # can't fetch more than 200 records from api/day
    if count > 200 : break
    address = line.strip()
    print ''
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (buffer(address), ))
    # look to see if we already have this address in the DB, if so we will skip
    try:
        data = cur.fetchone()[0]
        print "Found in database ",address
        # we already have address, so we skip inserting into db
        continue
    except:
        pass
    # this address not in db so go ahead and fetch the geo data for this location
    print 'Resolving', address
    url = serviceurl + urllib.urlencode({"sensor":"false", "address": address})
    print 'Retrieving', url
    #uh = urllib.urlopen(url, context=scontext)
    uh = urllib.urlopen(url,scontext)
    data = uh.read()
    print 'Retrieved',len(data),'characters',data[:20].replace('\n',' ')
    count = count + 1
    try:
        # parse the json into string
        js = json.loads(str(data))
        # print js  # We print in case unicode causes an error
    except:
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print '==== Failure To Retrieve ===='
        print data
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', ( buffer(address),buffer(data) ) )
    conn.commit()
    time.sleep(1)

print "Run geodump.py to read the data from the database so you can visualize it on a map."
