# file:         urlrewrite.py
# Author:       Nikhil Gorantla
# Data:         14/Jan/2018
# Description:  Fun little python program to show how can we use the regular expressions to change the url names from a multi line strings
#               This example is about re-writing URLs. It assumes we are moving a series
#               of web sites from the domain workspace.com to the domain newworkspace.org and
#               need to update a document containing a list of URLs.


#!/usr/bin/python3



import re

# This is the string containing the URLs we want to process.
# In reality we would more likely read this from a file.
# Multi line strings

urls = \
'''The report is <a href = https://docs.workspace.com/nikhil/report> here </a>
Access your mailbox <a href = http://mail.workspace.com/mailbox?id=1234"> here </a>
The full events list is at http://events.workspace.com/index.html'''

regex = r"(https?)://(\w+)\.workspace\.com/(\S+)"
newurls = re.sub(regex, r"\1://\2.newworkspace.org/\3", urls)
print(re.findall(regex, urls))   #  Debug only
print(newurls)
