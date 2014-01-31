#!/usr/bin/python

import sys

currentStudent = None
hours = {}


#TODO: verificar que los resultados son correctos
#TODO: ver si hay que filtrar por el tipo de node (p.ej, ¿cuentan los comentarios?)

def getMostFrequentHour(d):
	return sorted(d, key=d.get, reverse=True)[0]

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if (len(data_mapped) != 2):
		continue

	thisStudent, thisHour = data_mapped

	if currentStudent and currentStudent != thisStudent:
		h = getMostFrequentHour(hours)
		#print("{0}\t{1}".format(currentStudent, h))
		print("{0}\t{1}".format(currentStudent, hours))
		hours = {}
	
	currentStudent = thisStudent
	if thisHour in hours:
		hours[thisHour] += 1
	else:
		hours[thisHour] = 1


if currentStudent != None:
	h = getMostFrequentHour(hours)
	#print("{0}\t{1}".format(currentStudent, h))
	print("{0}\t{1}".format(currentStudent, hours))