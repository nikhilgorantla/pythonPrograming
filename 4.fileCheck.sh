# file:         fileCheck.sh
# Author:       Nikhil Gorantla
# Data:         1/Jan/2018
# Description:  Checking a file implementation in shell script 


#!/bin/bash
if [ -e /etc/hosts ]
then
    echo hosts file exists
else
    echo no hosts file
fi