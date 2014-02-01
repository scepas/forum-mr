#!/usr/local/bin/python

import sys
import csv

user_info = []
node_info = []
current_key = None

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    this_key = line[0]
    
    if current_key and current_key != this_key:
        user_info = []
        node_info = []

    current_key = this_key

    #user
    if (line[1] == 'YYYYYYYY'):
        user_info = line[2:]
        
    #node
    elif (line[1] == 'ZZZZZZZZ'):
        node_info = line[2:]
        assert (current_key == node_info[3])
        writer.writerow(node_info + user_info)   
        


