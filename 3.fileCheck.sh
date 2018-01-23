# Checking a file implementation in shell script 
#!/bin/bash
if [ -e /etc/hosts ]
then
    echo hosts file exists
else
    echo no hosts file
fi