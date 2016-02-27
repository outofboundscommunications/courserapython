

#example of using try/except to check dangerous input
istr = raw_input('enter a number:')
try:
    ival = int(istr)
except:
    ival = -1

if ival> 0:
    print ('nice job, ',ival, ' is a number')
else:
    print ('that is not a number...')
    istr = raw_input('enter a number:')

'''
   
astr = 'Hello Bob'
istr = int(astr)
print 'First', istr


astr = '123'
istr = int(astr)
print 'Second', istr
'''