#!/usr/bin/python3

class about_me:
			#__init__ is just like constructors in C++
	def __init__(self,name,college,year):
		self.name = name              #these three are instances
		self.college = college
		self.year = year


	def my_name(self):
		print("Hello, my name is", self.name)

	def clg_name(self):
		print("I am in",self.college,"college")

	def cur_year(self):
		print("I read in",self.year,"year")

	branch = "CSE"    #this is class variable

A = about_me("Shiv Soni","JECRC","3rd")
"""
A.my_name()	
A.clg_name()
A.cur_year()	
"""
print(A.year)
print(A.college)
print(A.name)
print(A.branch)          
print(about_me.branch)   #class variable can be accessed using class name also

