#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import getopt

def usage():
    print
    print "$ fileread -f filename"
    print
    sys.exit(0)

def main():

	if not len(sys.argv[1:]):
		usage()

	try:
		opts, args = getopt.getopt( sys.argv[1:], "f:")

	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o,a in opts:
		if o in ("-f"):
			filename = a

	fin = open(filename, 'rt')

	while True:
		line = fin.readline()
		if not line:
			break
		print line

	fin.close()

main()
