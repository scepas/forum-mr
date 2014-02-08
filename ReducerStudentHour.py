#!/usr/local/bin/python

import sys
from collections import Counter

current_student = None
hours = []

#return the top 1 most common hour
#if there are hours with equal count, an arbitrary one is returned
def get_most_frequent_hour(h):
    return Counter(h).most_common(1)[0][0]

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if (len(data_mapped) != 2):
        continue

    this_student, this_hour = data_mapped

    if current_student and current_student != this_student:
        h = get_most_frequent_hour(hours)
        print("{0}\t{1}".format(current_student, h))
        hours = []
    
    current_student = this_student
    hours.append(this_hour)
    
if current_student:
    h = get_most_frequent_hour(hours)
    print("{0}\t{1}".format(current_student, h))
