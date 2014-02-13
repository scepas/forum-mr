#!/usr/local/bin/python

import sys
from collections import Counter

current_student = None
hours = []

#return the top 1 most common hour
#if there are ties, all hours with the same count are returned 
def get_most_frequent_hour(h):
    c = Counter(h)
    #number of times the most common hour appears
    top = c.most_common(1)[0][1]
    #return all hours appearing top number of times
    return [hour for hour, count in c.items() if count == top]
    

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
