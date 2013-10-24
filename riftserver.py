#!/usr/bin/env python 
import urllib2
from bs4 import BeautifulSoup

site = urllib2.urlopen('http://status.riftgame.com/na-status.xml')
status = site.read()
soup = BeautifulSoup(status)

#Retreive the first table, returning the data we're looking for. 
#Needs more filtering.
table = soup.find("table")

rows=list()
for row in table.findAll("tr"):
   rows.append(row)

for row in rows:
		print row

