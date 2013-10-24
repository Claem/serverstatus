#!/usr/bin/env python 
import urllib2
from xml.dom import minidom

site = urllib2.urlopen('http://status.riftgame.com/na-status.xml')
status = site.read()
xmldoc = minidom.parseString(status)
itemlist = xmldoc.getElementsByTagName('shard')

for s in itemlist :
    if s.attributes['name'].value == 'Faeblight' :
      #  print s.attributes['online'].value
        if s.attributes['online'].value == 'True'  :
            print 'Go Play!'



