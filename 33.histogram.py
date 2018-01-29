# file:         histogram.py
# Author:       Nikhil Gorantla
# Data:         14/Jan/2018
# Description:  This python program this will access the apache access logs and 
#               count the url's in the apache log and give us how many times that specific URl is access in a histogram.  


#!/usr/bin/python3


import collections

# New dictionary entries default to integer value of zero
hist = collections.defaultdict(int)

for line in open("/var/log/httpd/access_log"):
    # Isolate the URL (file name) from the access log entry
    url = line.split()[6].split('?')[0]
    # and count another hit for that page
    hist[url] += 1

# Loop over dictionary entries sorted by value
for url in sorted(hist, key=hist.get, reverse=True):
    # Stop printing when hit counts fall below zero
    if hist[url] < 50:
        break;
    print ("%-40s : %6d" % (url, hist[url]))