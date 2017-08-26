#!/usr/bin/python2

#CLASSIC ALGORITHM 1
#Collatz Conjecture

num=input("Enter the number greater than 1: ")
c=0
while num!=1:
	if num%2==0:
		num=num/2
		c=c+1
	else :
		num=(num*3)+1
		c=c+1

print("Total number of steps to reach 1 are: "+str(c))
