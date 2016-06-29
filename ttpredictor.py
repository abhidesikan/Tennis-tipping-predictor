#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen("http://www.oddschecker.com/tennis/wimbledon/mens/winner").read()
soup = BeautifulSoup(page)
print(soup.prettify())


