#!/usr/bin/python3

#IF A CLASS IS SUBCLASS OF ANOTHER OR NOT

class base(object):
	pass 		#Empty class

class derived(base):
	pass

print(issubclass(derived, base))	#issubclass python function
print(issubclass(base, derived))	#

d = derived()
b = base()


print(isinstance(b, derived))		#isinstance python function--b is not an
print(isinstance(d, base))		#instance of derived while d is of base
