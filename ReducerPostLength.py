#!/usr/local/bin/python

import sys

current_id = None
answers_length = []
question_length = 0

#input: id\t\isquestion\tlength

def get_average(l):
    if len(l) == 0:
        return 0
    else: 
        return sum(l) / len(l)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if (len(data_mapped) != 3):
        continue

    this_id, this_type, this_length = data_mapped
    this_length = int(this_length)
    
    if current_id and current_id != this_id:

        print("{0}\t{1}\t{2}".format(current_id, question_length, get_average(answers_length)))
        answers_length = []
        question_length = 0

    current_id = this_id
    #question
    if this_type == "0":
        question_length = this_length
    #answer
    elif this_type == "1":
        answers_length.append(this_length)

if current_id:
    print("{0}\t{1}\t{2}".format(current_id, question_length, get_average(answers_length)))
