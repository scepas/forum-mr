#!/usr/local/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n\r')

for line in reader:
    #if it's the header, we skip it
    if line[0] == "id":
        continue

    tags = line[2].split()
    for tag in tags:
        print("{0}\t{1}".format(tag, 1))
        


