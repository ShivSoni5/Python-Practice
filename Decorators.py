#!/usr/bin/python

from functools import wraps

def add_wrapping(item):
#	@wraps(item)
	def wrapped_item():
		return 'a wrapped up box of {}'.format(str(item()))   #it treats "item" as a function thats why need to use item()
	return wrapped_item	



"""
def add_wrapping1(item):
	def wrapped_item():
		return 'a wrapped up box of {}'.format(str(item()))
	return wrapped_item
"""
@add_wrapping
def new_laptop():
	return "dell xps 1300"

print(new_laptop())
print(new_laptop.__name__)
"""
@add_wrapping1    
def new_200ns():
	return "laptop on my new bike pulsar 200ns"


print(new_200ns())
print(new_200ns.__name__)
"""

