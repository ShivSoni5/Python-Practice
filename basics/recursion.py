#!/usr/bin/python

import sys
sys.setrecursionlimit(1500)

i=1
def count(a):
	print a
	count(a+1)
"""	recur(a+1)		

def recur(b):
	print b
	count(b+1)
"""
count(i)
