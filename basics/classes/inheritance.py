#!/usr/bin/python3


class superclass:
	
	def __init__(self,name):
		self.name = name

	def getname(self):
		return self.name

	def isEmployee(self):
		return False

class employee(superclass):   #inherited superclass
	
	def isEmployee(self):
		return True

A = superclass("Shiv")
print(A.getname(), A.isEmployee())

B = employee("Raj")
print(B.getname(), B.isEmployee())
