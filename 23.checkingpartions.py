# file:         checkingpartions.py
# Author:       Nikhil Gorantla
# Data:         14/Jan/2018
# Description:  This python program shows the practical use of optparse. 
#               Here we are checking the partions in the linux with help of a threshold so we can monitor continuously 


#!/usr/bin/python3

from optparse import OptionParser
import time
from check_partitions_funcs import *

# Parse the command options and partition list
parser = OptionParser()
parser.add_option("-t", "--threshold",
                  dest="threshold",
                  type="int",
                  default=90,
                  help="Set threshold (%)")
parser.add_option("-s", "--single",
                  action="store_true",
                  dest="singleshot",
                  default=False,
                  help="just check once, don't loop")
parser.add_option("-m", "--mailbox",
                  dest="mailbox",
                  help="mail report to this mailbox")

# For verification, print out our options and arguments
(options, partition_list) = parser.parse_args()
print("singleshot is %r" % options.singleshot)
print("mailbox is %s" % options.mailbox)
print("threshold is %d" % options.threshold)
print("partition list is %s" % str(partition_list))

# Main loop
while True:
    check_once(options, partition_list)
    if options.singleshot:
        exit(0)
    time.sleep(5)
