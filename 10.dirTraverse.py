# file:         dirTraverse.py
# Author:       Nikhil Gorantla
# Data:         1/Jan/2018
# Description:  This is implementation of directory traverse and get what the contents inside the directories 
#               From os module we are using os.walk in order to traverse thought the file system and get the data we need


#!/usr/bin/python3

import os

dirName = input("Enter the Directory name to list the size of the files: ")
for dirpath, dirnames, filenames in os.walk(dirName):

    print("Files in %s are:" % dirpath)
    for file in filenames:
        print("\t" + file)

    print("Directories in %s are: " %dirpath)
    for dir in dirnames:
        print("\t" + dir)    