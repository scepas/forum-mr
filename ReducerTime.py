#!/usr/local/bin/python

import sys
import datetime

current_node = None
question_time = None
answer_time = None

def get_time(s):
    return datetime.datetime.strptime(s[0:19], "%Y-%m-%d %H:%M:%S")

def get_delta(q, a):
    if (a == None or q == None):
        return ""
    else:
        return int((a - q).total_seconds())

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if (len(data_mapped) != 3):
        continue

    this_node, this_type, this_time = data_mapped

    if (current_node and current_node != this_node):
        print "{0}\t{1}".format(current_node, get_delta(question_time, answer_time))
        question_time = None
        answer_time = None

    current_node = this_node
    if (this_type == "1"):
        question_time = get_time(this_time)
    elif (this_type == "2"):
        if (not answer_time):
            answer_time = get_time(this_time)
        else:
            continue

if current_node:
    print "{0}\t{1}".format(current_node, get_delta(question_time, answer_time))





