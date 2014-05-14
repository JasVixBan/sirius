#!/bin/python
import string
import sys
import re

if( len(sys.argv) == 1 or len(sys.argv) != 3 ):
	print "Usage: print-parse.py <svm-scores-file> <sentence-file>"
	sys.exit(1)

score_file_lines = open(sys.argv[1]).readlines()

list_of_start_arrays = []
list_of_end_arrays   = []
list_of_role_arrays  = []
list_of_target_indices = []
list_of_word_lists = []
start_array = []
end_array   = []
role_array  = []

word_list   = []

i=0
for i in range(0, len(score_file_lines)):
	if(len(string.strip(score_file_lines[i])) == 0):
		list_of_start_arrays.append(start_array)
		list_of_end_arrays.append(end_array)
		list_of_role_arrays.append(role_array)
		list_of_target_indices.append(target_index)
		start_array = []
		end_array   = []
		role_array  = []
		continue

	list = string.split(score_file_lines[i])
	#print list
	#print list[2]
	#print list[3]
	#print list[13]
	start_array.append(string.atoi(list[2]))
	end_array.append(string.atoi(list[3]))
	role_array.append(list[13])
	target_index = string.atoi(list[1])

list_of_word_lists = open(sys.argv[2]).readlines()

kk=0
for kk in range(0, len(list_of_word_lists)):
	list_of_word_lists[kk] = string.split(list_of_word_lists[kk])

#word_list = string.split(open(sys.argv[2]).readlines()[0])

#print len(list_of_start_arrays)
#print len(list_of_word_lists)

jj=0
for jj in range(0, len(list_of_start_arrays)):
	#word_list_copy = [] + word_list
	word_list_copy  = list_of_word_lists[jj]
	
	word_list_copy[list_of_target_indices[jj]] = "<font color=\"#FF6666\">[<sub>target</sub> <i>%s " % (word_list_copy[list_of_target_indices[jj]])
	word_list_copy[list_of_target_indices[jj]]   = "%s</i> ]</font>" % (word_list_copy[list_of_target_indices[jj]])

	j=0
	for j in range(0, len(list_of_start_arrays[jj])):
		if( list_of_role_arrays[jj][j] == "O" ):
			continue
		word_list_copy[list_of_start_arrays[jj][j]] = "<font color=\"#FF6666\">[<sub>%s</sub></font> <i><font color=\"#3333FF\">%s" % (string.lower(list_of_role_arrays[jj][j]), word_list_copy[list_of_start_arrays[jj][j]])
		word_list_copy[list_of_end_arrays[jj][j]]   = "%s</font></i><font color=\"#FF6666\">]</font>" % (word_list_copy[list_of_end_arrays[jj][j]])

	print string.join(word_list_copy)
	print "<hr>"
	
	
	
