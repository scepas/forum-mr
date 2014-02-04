#!/usr/local/bin/python

import sys

students = []
current_node = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if (len(data_mapped) != 2):
        continue

    this_node, this_student = data_mapped
    if (current_node and current_node != this_node):
        print("{0}\t{1}".format(current_node, students))
        students = []

    current_node = this_node
    students.append(this_student)

if current_node:
    print("{0}\t{1}".format(current_node, students))