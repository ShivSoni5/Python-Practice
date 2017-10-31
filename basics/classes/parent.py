#!/usr/bin/python

# Python example to show that base
# class members can be accessed in
# derived class using base class name
class Base(object):

	# Constructor
	def __init__(self, z):
		self.x = z
		
	def return_x(self ,p):
		self.z = self.x + p
		return self.z

class Derived(Base):

	# Constructor
	def __init__(self, y):
		Base.x = "shiv" 
		self.y = y

	def printXY(self):
	
		print(self.x, self.y) 
	    	#print(Base.x, self.y)


# Driver Code
d = Derived(20)
d.printXY()
b=Base(30)
a=b.return_x(20)
print(a)

