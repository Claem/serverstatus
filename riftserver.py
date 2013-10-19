#!/usr/bin/env python 
import urllib2

site = urllib2.urlopen('http://www.riftgame.com/en/shardstatus/')
status = site.read()
print status
