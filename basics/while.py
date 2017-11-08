#!/usr/bin/python2

i=0

while i<3:
	a=raw_input("enter password:")
	if a=="redhat":
		print "welcome"
		break
	else:
		print "wrong password"
	i=i+1
