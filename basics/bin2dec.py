#!/usr/bin/python2


num=raw_input("Enter the binary number: ")

c=len(num)-1
_sum=0
flag=0

for i in num:
	if int(i) == 1 or int(i) == 0 :
		flag=0
	elif int(i) in range(2,10) :
		flag=1
		break

if flag==1:
	print("The given number is not binary")


for i in range(len(num)):
	_sum = int(num[i])*(2**c) + _sum
	c=c-1

if flag==0:
	print("The decimal equivalent to the given binary number is "+str(_sum))

