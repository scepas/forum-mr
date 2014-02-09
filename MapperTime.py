#!/usr/local/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    #if it's the header, we skip it
    if line[0] == "id":
        continue

    #if is a question we're interested on the id
    if line[5] == "question":
        id = line[0]
        node_type = "1"
    elif line[5] == "answer":
        id = line[7]
        node_type = "2"
    else:
        continue

    print "{0}\t{1}\t{2}".format(id, node_type, line[8])