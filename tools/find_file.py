#!/usr/bin/env python
from __future__ import print_function
import os
import fnmatch
import argparse


def isMine(item, patterns):
	for pattern in patterns:
		if fnmatch.fnmatch(item, pattern):
			return True
	return False

def find_files(dir, patterns=['*'], exclude_dir = []):
	if not os.path.exists(dir):
		raise 'the dir no exists.'

	for root, dirnames, filenames in os.walk(dir):
		for item in filenames:
			if isMine(item, patterns):
				yield os.path.join(root, item)
		for d in exclude_dir:
			if d in dirnames:
				dirnames.remove(d)
		
def get_argparser():
	parser = argparse.ArgumentParser(description='find files')
	parser.add_argument('-d', action='store', dest='dir', required=True,\
	 help='The directory to look for')
	parser.add_argument('-p', action='store', nargs='*',dest='patterns',\
	 required=False, help='A matching file suffix is required')
	parser.add_argument('-e', action='store', nargs='*',dest='exclude_dir',\
		required=False, help="Directories you don't need to look for")
	return parser.parse_args()

def main():
	parser = get_argparser()
	dir = parser.dir
	patterns = parser.patterns
	exclude_dir = parser.exclude_dir

	if not patterns:
		patterns = ['*']
	if not exclude_dir:
		exclude_dir = []
	for i in find_files(dir, patterns, exclude_dir):
		print(i)


def get_size_file():
	files = {name: os.path.getsize(name) for name in \
	find_files('/home/yang/Document/Demo/test_Demo/')}
	results = sorted(files.items(), key=lambda d:d[1], reverse=1)[:10]
	for i, t in enumerate(results, 1):
		print(i, t[0], t[1])	

if __name__ == '__main__':
	# main()
	get_size_file()


