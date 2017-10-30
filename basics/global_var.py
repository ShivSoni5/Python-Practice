#!/usr/bin/python

#read every comment

x = 6 

def new():
	print x	    #we can access x but cannot modify it in next step
	global x    #so to modify it we will use global keyword as shown
	x += 5
	print x 

new()

y = 6

def change():
	print y     #we know we can access x(here y)..but dont want use global variable soo
	globv = y
	globv += 5
	print globv

change()

#output: same result using global or by passing to another value



#value of x is modified but not of y..so to modify it we can modify change as change1()

z = 6

def change1():
	print z
	globv = z
	globv += 5
	print globv
	return globv

z = change1()

print("x = "+str(x))
print("y = "+str(y))
print("z = "+str(z))
