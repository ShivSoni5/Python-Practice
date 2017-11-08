#!/usr/bin/python2

num=input("Enter the number whose factorial will be calculated:")

product=1

if num<0:
	print"Well, n! is for integer n < 0 not defined. Sorry!"
elif num == 0:
	print("0!=1")
else:
	while num!=1:
		product=num*product
		num=num-1

	print product
