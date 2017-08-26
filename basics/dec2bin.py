#!/usr/bin/python2

import sys


num=input("Enter the decimal number:" )
lis=[]
while num!=0 :
	if num % 2 == 0:
		num=num/2
		lis.append(0)
	else:
		num=(num-1)/2
		lis.append(1)

for i  in lis[::-1]:
	sys.stdout.write(str(i))
print ""
