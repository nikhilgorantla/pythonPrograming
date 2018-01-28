# file:         echo.py
# Author:       Nikhil Gorantla
# Data:         14/Jan/2018
# Description:  Fun little python program to relicate the echo in bash 

import sys

for arg in sys.argv[1:]:
    print(arg, end=' ')
print()

