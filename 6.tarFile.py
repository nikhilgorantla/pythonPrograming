import tarfile          #this module will help to tar files 
import glob             #module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order

filePath = input("enter the file path: ")

def create_tarfile():
    tFile = tarfile.open("tarfile1.tar", "w")
    for configFile in glob.glob(filePath):
        tFile.add(configFile)
    tFile.close()

create_tarfile()
    