#This is 2nd version of implementation of tar archive 

import tarfile
import glob

filePath = input("Enter the file path here: ")
fileName = input("Enter the tar file name: ")
tfile = tarfile.open(fileName, "w")

for configfile in glob.glob(filePath):
    tfile.add(configfile)

tfile.close()