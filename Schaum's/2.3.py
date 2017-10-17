#!/usr/bin/python

data=list(input("enter the data : "))

l=len(data)

loc1,loc2=0,1
first,second=data[0],data[1]

if first<second:
	first,second=second,first
	loc2,loc1=0,1

for i in range(2,l):
	if first<data[i]:
		second=first
		first=data[i]
		loc=loc1
		loc1=i
	elif second<data[i]:
		second=data[i]
		loc2=i

print "first largest: "+ str(loc1+1)	
print "second largest: "+ str(loc2+1)	
