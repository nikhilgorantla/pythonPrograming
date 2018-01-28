# file:         fileWalk.py
# # Author:     Nikhil Gorantla
# Data:         14/Jan/2018
# Description:  simple file Walk demo with os walk which displaoys files recursively


#!/usr/bin/python



import os

fpath = input("enter the directory name to lsit all the files recursively: ")
for dirpath, dirnames, filenames in os.walk("."):
    print("Files in %s are:" % dirpath)
    for file in filenames:
        print("\t" + file)
    print("Directories in %s are:" % dirpath)
    for dir in dirnames:
        print("\t" + dir)