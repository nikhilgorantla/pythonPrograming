# file:         fileCheck.py
# Author:       Nikhil Gorantla
# Data:         1/Jan/2018
# Description:  This is a simple program to check weather their is file or not 
#               Importing Os module to achive our goal 

#!/usr/bin/python3

import os.path

if os.path.exists("/etc/hosts"):
    print("hosts file exists")
else:
    print("Hosts file doesnt exits")