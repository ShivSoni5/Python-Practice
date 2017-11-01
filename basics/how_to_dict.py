#!/usr/bin/python

#HOW TO USE DICTIONARY

#creating empty dictionary

x = {}
print "\nx =",x

#inserting values in x
print "\ninserting values into x"
x = {0: 1, 3: 5, 10: "raj", "shiv": 6} 
print "x =",x

#adding a value to dict
x[2] = 22
#value inside square bracket are keys and 22 is value at key

print "\nafter adding a value(2:22) to x \n",x

print "\nall keys",x.keys()
print "\nall values",x.values()

#getting value from key
print "\ngetting value at key 0 and 3"
print "x[0] =",x[0]
print "x[3] =",x[3]

#getting keys from values
print "\ngetting keys from values 'raj' and 6"
print "raj is present at key", x.keys()[x.values().index("raj")]
print "6 is present at key", x.keys()[x.values().index(6)]

#deleting value at particular key
print "\ndeleting value at key 0"
del x[0]
print x


