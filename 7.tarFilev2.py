# file:         tarFile.py
# Author:       Nikhil Gorantla
# Data:         1/Jan/2018
# Description:  This program will tar the file's in the given directory
#               Improvised version of implementation of tar archive 

import tarfile
import glob

filePath = input("Enter the file path here: ")
fileName = input("Enter the tar file name: ")
tfile = tarfile.open(fileName, "w")

for configfile in glob.glob(filePath):
    tfile.add(configfile)

tfile.close()