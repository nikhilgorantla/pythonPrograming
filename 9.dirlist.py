# This is simple Directory listing program and which give the size of the files 
#!/usr/bin/python3

import os

dirName = input("Enter the Directory name to list the size of the files: ")
for file in os.listdir(dirName):
    info = os.stat(file)
    print("%-20s : size %d" % (file, info.st_size))


# file:         largestUID.sh
# Author:       Nikhil Gorantla
# Data:         1/Jan/2018
# Description:  This is showcasing the diffrence between python and bash to largest UID
# Reference:    Check 1.maxuid.py for reference