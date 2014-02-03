#!/usr/local/bin/python

##########################################################
# This script works both as combiner and as reducer
# The Map Reduce job SHOULD be configured with a combiner
# to make sure the top ten tags are properly accounted for
##########################################################

import sys

current_tag = None
count = 0

list_tags = []
k = 10

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if (len(data_mapped) != 2):
        continue

    this_tag, this_count = data_mapped
    this_count = int(this_count)
    if current_tag and current_tag != this_tag:
        if len(list_tags) < k:
            list_tags.append((current_tag, count))
        elif (list_tags[0][1] < count):
            list_tags[0] = (current_tag, count)    
        
        list_tags = sorted(list_tags, key = lambda b:b[1])
        count = 0

    current_tag = this_tag
    count += this_count

for t, c in sorted(list_tags, key = lambda b:b[1], reverse = True):
    print("{0}\t{1}".format(t, c))    

