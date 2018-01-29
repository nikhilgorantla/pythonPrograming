# file:         CheckingTararchive.py
# Author:       Nikhil Gorantla
# Data:         14/Jan/2018
# Description:  This python program helps Extract only recently modified files (using tarinfo)

#!/usr/bin/python3

import os
import tarfile
import time

dPath = input("Enter the directory name: ")
os.chdir(dPath)

# Compute the time one week ago (seconds since epoch)
mintime = time.time() - (7 * 24 * 3600)

with tarfile.open("/logs/log1.tar", "r") as t:
    for info in t:
        if info.mtime > mintime and info.isfile():
            print("extracting %s" % info.name)
            t.extract(info)