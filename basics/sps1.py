#!/usr/bin/python2
#stone-paper-scissors

import random

a1=0
u1=0
flag=0

x="""
 ------------------------------------------------------------------------------
 ------------------------------------------------------------------------------

			STONE-PAPER-SCISSORS

 ------------------------------------------------------------------------------
 ------------------------------------------------------------------------------
   

 Enter 1  for Stone, 2 for Paper, 3 for Scissors

"""
tup=("stone","paper","scissors")
print x

q=input("how many times you want to play: ")

for i in range(q):
	b=input(str(i+1)+". Enter your choice: ")
	c=random.choice(tup)
	print ("Computers choice is: "+c)
	if b not in range(1,4):
		print("Wrong input,should be 1, 2 or 3")

	elif b==1 :
		if c=='stone':
			a1=a1+1
			u1=u1+1
		elif c=='paper':
			a1=a1+1
		elif c=='scissors':
			u1=u1+1

	elif b==2 :
		if c=="stone":
                        u1=u1+1
                elif c=="paper":
			a1=a1+1
                        u1=u1+1
                elif c=="scissors":     
                        a1=a1+1
	elif b==3 :
		if c=="stone":
                        a1=a1+1
                elif c=="paper":
                        u1=u1+1
                elif c=="scissors":     
                        a1=a1+1
			u1=u1+1

	print ("score: "+str(u1)+":"+str(a1)+"\n")
	print("Chances ramaining: "+str(q-(i+1)))


if a1>u1:
	print("You lose  by score "+str(u1)+":"+str(a1))
elif a1==u1:
	print("Game is Draw by score "+str(u1)+":"+str(a1))
else :
	print("You won by score "+str(u1)+":"+str(a1))
