# file:         largestUID.sh
# Author:       Nikhil Gorantla
# Data:         1/Jan/2018
# Description:  This is showcasing the diffrence between python and bash to largest UID

sort -n -t: -k3 /etc/passwd | tail -1 | cut -d: -f3 