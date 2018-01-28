# file:         killinguserprocess.py
# Author:       Nikhil Gorantla
# Data:         1/Jan/2018
# Description:  Python program to kill all the processes owned by a specified user.

#!/usr/bin/python3

import pwd
import glob
import os
import signal

def getprocessuid(procdir):
    statusfile = open(procdir + "/status")
    for line in statusfile:
        if line.startswith("Uid:"):
            splitline = line.split()
            uid = int(splitline[2])
            return uid

# Will take this from command line eventually
username = input("Enter the Username: ")

try:
    pwdentry = pwd.getpwnam(username)
except KeyError:
    print("error: no such user ... giving up!")
    exit(1)

targetuid = pwdentry.pw_uid

print("target uid is %d" % targetuid)

os.chdir("/proc")

procdirlist = glob.glob("[0-9]*")

for procdir in procdirlist:
    if getprocessuid(procdir) == targetuid:
        print("killing process %s" % procdir)
        os.kill(int(procdir), signal.SIGTERM)



