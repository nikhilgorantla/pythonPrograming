# file:         BrokenSymlinks.py
# Author:       Nikhil Gorantla
# Data:         14/Jan/2018
# Description:  This program disploays the broken symbolic links 

import os

testdir = input("enter the directory name to chcek the broken symbolic links: ")

uidset = set()
for line in open("/etc/passwd"):
    split = line.split(":")
    uidset.add(int(split[2]))

for folder, dirs, files in os.walk(testdir):
    for file in files:
        path = folder + "/" + file

        try:
            attributes = os.stat(path)
        except FileNotFoundError:
            print(path + ":  not found")
            continue
