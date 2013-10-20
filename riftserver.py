#!/usr/bin/env python 
import urllib2
from bs4 import BeautifulSoup

site = urllib2.urlopen('http://www.riftgame.com/en/shardstatus/')
status = site.read()
soup = BeautifulSoup(status)
text = soup.body.find_all(text=True)

print text

