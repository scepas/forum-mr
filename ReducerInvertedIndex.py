#!/usr/local/bin/python

import sys

current_line = None
current_word = None
nodes = set()


for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if (len(data_mapped) != 2):
		continue

	#if we've already processed this word-node combination, skip it
	if current_line and current_line == data_mapped:
		continue

	this_word, this_node_id = data_mapped

	if current_word and current_word != this_word:
		print("{0}\t{1}".format(current_word, sorted(nodes)))
		current_word = this_word;
		nodes = set()

	current_line = data_mapped
	current_word = this_word
	nodes.add(int(this_node_id))

if current_word:
	print("{0}\t{1}".format(current_word, sorted(nodes)))
