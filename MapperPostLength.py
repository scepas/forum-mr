#!/usr/local/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n\r')

for line in reader:
    #if node_type is question
    node_type = line[5]
    is_question = 0

    id = None
    if node_type == "question":
        id = line[0]
        is_question = 0
    elif node_type == "answer":
        id = line[7]
        is_question = 1
    else:
        continue

    length = len(line[4])

    print("{0}\t{1}\t{2}".format(id, is_question, length))