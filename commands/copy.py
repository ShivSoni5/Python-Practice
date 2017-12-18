#!/usr/bin/python

import os,sys

#s=raw_input("Enter the directory of file to be copied: ")
#os.chdir(s)

s=sys.argv[1]
r=sys.argv[2]

#r=raw_input("enter file: ")
#f=open(r,"r")
#d=raw_input("Enter the destination directory of file be copied: ")
#os.chdir(d)

def copy(a,b):
	
	f=open(a,"r")
	x = f.read()
	f.close()

	try:
	
		f1= open(b,"w")
		f1.write(x)
		f1.close()
	
	except IOError:        #when name is not provided eg.  cp /root/Desktop/shiv.py /root/Document/
		os.chdir(b)
		c=a.split('/')
		f1=open(c[-1],"w")
		f1.write(x)
		f1.close()

copy(s,r)
		
	
