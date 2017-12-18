#usr/bin/python

import os,sys

s=raw_input("Enter the directory of file to be copied: ")

os.chdir(s)

r=raw_input("enter file: ")
f=open(r,"r")

x = f.read()

f.close()
d=raw_input("Enter the destination directory of file be copied: ")

os.chdir(d)

f1= open(r,"w")
f1.write(x)

f1.close()
