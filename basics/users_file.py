#!/usr/bin/python2

import commands

y=raw_input("enter the file containing list:")

i= commands.getoutput("wc -l <"+y)
n=int(i)
for x in range(n):
	c=commands.getoutput("head -"+str(x)+" "+y+"| tail -1 ")
	commands.getoutput("useradd "+ c)
	d=(c+"@123")
	commands.getoutput("echo "+d+" | passwd "+c+" --stdin")
