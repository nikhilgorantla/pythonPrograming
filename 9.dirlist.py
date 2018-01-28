# file:         dirlist.py
# Author:       Nikhil Gorantla
# Data:         1/Jan/2018
# Description:  This is simple Directory listing program and which give the size of the files in the given directory



#!/usr/bin/python3

import os

dirName = input("Enter the Directory name to list the size of the files: ")
for file in os.listdir(dirName):
    info = os.stat(file)
    print("%-20s : size %d" % (file, info.st_size))