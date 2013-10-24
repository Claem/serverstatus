#!/usr/bin/env python 
import urllib2
from xml.dom import minidom

site = urllib2.urlopen('http://status.riftgame.com/na-status.xml')
status = site.read()

print status 

