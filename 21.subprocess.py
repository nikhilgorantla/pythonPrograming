# file:         subprocess.py
# Author:       Nikhil Gorantla
# Data:         14/Jan/2018
# Description:  This python program shows the way to implement the shell commands in the python program using subprocess module
#               Demonstrate piping out of a child process
#               Print names of files bigger than 10000 bytes


#!/usr/bin/python3
from subprocess import Popen, PIPE

lister = Popen(["ls", "-l"], stdout=PIPE)

for bytes in lister.stdout:
    line = bytes.decode()
    if line.startswith("total"):
        continue
    splitline = line.split()
    # Size is in field 4, name in field 8
    if int(splitline[4]) > 1000:
        print(splitline[8])