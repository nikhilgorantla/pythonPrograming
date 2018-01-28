# file:         uidSetv2.py
# Author:       Nikhil Gorantla
# Data:         1/Jan/2018
# Description:  This program will give the list of UID of users in the system in a list format


import pwd
uidset = set()
for user in pwd.getpwall():
    uidset.add(user.pw_uid)

print(uidset)