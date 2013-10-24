#!/usr/bin/env python 
import urllib2
from xml.dom import minidom

site = urllib2.urlopen('http://status.riftgame.com/na-status.xml')
status = site.read()
xmldoc = minidom.parseString(status)
itemlist = xmldoc.getElementsByTagName('shard')

print len(itemlist)
print itemlist[0].attributes['name'].value
for s in itemlist :
    print s.attributes['name'].value




