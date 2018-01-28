# file:         simple-ls
# Author:       Nikhil Gorantla
# Data:         14/Jan/2018
# Description:  fun little program to list all the files in the directory with their sizes.

import os

fpath = input("please enter the dir to check list of files with sizes: ")
for file in os.listdir(fpath):
    info = os.stat(file)
    print("%-20s : size %d" % (file, info.st_size))

    