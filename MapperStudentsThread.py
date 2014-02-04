#!/usr/local/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n\r')

for line in reader:
    #if it's the header, we skip it
    if line[0] == "id":
        continue

    #if question, id = node_id; if comment id = abs_parent_id
    if line[5] == "question":
        id = line[0]
    else:
        id = line[7]
    
    print("{0}\t{1}".format(id, line[3]))