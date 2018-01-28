# file:         uidSet.py
# Author:       Nikhil Gorantla
# Data:         1/Jan/2018
# Description:  This program will give the list of UID of users in the system in a list format

uidset = set()
for line in open("/etc/passwd"):
    split = line.split(":")
    uidset.add(int(split[2]))

print (uidset)
# print(*uidset,sep='\n')