#!/usr/bin/python

import argparse
import os
import sys
import random

def parse_args():
	parser = argparse.ArgumentParser(description='Santa Py',
		formatter_class=argparse.RawDescriptionHelpFormatter,
		epilog='''
		test Py
		''')
	parser.add_argument('-n', '--new', action='store',
		dest='first_file',
		default='--',
		required=True,
		help='1st set of names')
	parser.add_argument('-o', '--old', action='store',
		dest='second_file',
		default='--',
		required=False,
		help='2nd set of names')
	parser.add_argument('-v', '--version',
		action='version',
		version='%(prog)s 0.01')
	return parser.parse_args()

def parse_file (filename, dic):
	with open(filename, 'r') as f:
		for line in f:
			dic.append(line.strip())


if __name__ == '__main__':
	PARAM = parse_args()
	new_filename = PARAM.first_file
	old_filename = PARAM.second_file
	
	if os.path.exists(new_filename) == False:
		print 'following file does not exist:', new_filename
		sys.exit()

	if old_filename == '--':
		old_filename = new_filename

	first_list = []
	parse_file (new_filename,first_list)
	second_list = []
	parse_file (old_filename,second_list)

	random.shuffle(first_list)
	random.shuffle(second_list)

	if len(first_list) != len (second_list):
		print "Size of the lists not matching"
		sys.exit()

	for first_name in first_list:
		matched_name = random.choice([second_name for second_name in second_list if second_name != first_name])
		print(first_name,matched_name)
		second_list.remove(matched_name)
