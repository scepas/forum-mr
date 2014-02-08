#!/usr/local/bin/python

import sys


current_word = None
nodes = []

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if (len(data_mapped) != 2):
		continue

	this_word, this_node_id = data_mapped

	if current_word and current_word != this_word:
		print("{0}\t{1}".format(current_word, sorted(nodes)))
		current_word = this_word;
		nodes = []

	current_word = this_word
	nodes.append(int(this_node_id))

if current_word:
	print("{0}\t{1}".format(current_word, sorted(nodes)))