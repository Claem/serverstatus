#!/usr/bin/env python 
import urllib2
from xml.dom import minidom
import sys

def onlinestat(server):
    site = urllib2.urlopen('http://status.riftgame.com/na-status.xml')
    status = site.read()
    xmldoc = minidom.parseString(status)
    itemlist = xmldoc.getElementsByTagName('shard')
    for s in itemlist:
        if s.attributes['name'].value == server:
            return s.attributes['online'].value
            

if onlinestat('Faeblight') == 'True':
    print 'Go Play!'
    
    