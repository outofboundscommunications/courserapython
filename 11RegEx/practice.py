__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#
import re

s = '''
stephen.marquard@uct.ac.za, csev@umich.edu, and cwen @iupui.edu
Return-Path: <postmaster@collab.sakaiproject.org>
for <source@collab.sakaiproject.org>;
Received: (from apache@localhost)
Author: stephen.marquard@uct.ac.za
'''
lst = re.findall('.+?@.+', s)
print 'the list size is:', len(lst)
for theItem in lst:
    print theItem
    
    
'''
stephen.marquard@u                                                              
ct.ac.za, csev@u                                                                
mich.edu, and cwen @i                                                           
Return-Path: <postmaster@c                                                      
for <source@c                                                                   
Received: (from apache@l                                                        
Author: stephen.marquard@u 

'''