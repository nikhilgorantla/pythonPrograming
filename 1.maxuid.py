# file:         maxuid.py
# Author:       Nikhil Gorantla
# Data:         1/Jan/2018
# Description:  Finding the max UID of a user in /etc/passwd 


maxuid = 0
for line in open("/etc/passwd"):
    split = line.split(":")
    if int(split[2]) > maxuid:
            maxuid = int(split[2])
            
print(maxuid)