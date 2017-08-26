a=input("enter first character of tuple x:")
b=input("enter second character of tuple x:")
c=input("enter third character of tuple x:")
d=input("enter fourth character of tuple x:")
x=a,b,c,d
print "x=(a,b,c,d)"
y=16
print "y = 16"
z=20
print "z = 20"
p=[y,z,x]
print "p=[y,z,x]"
print p
if type(p[2][0])==str:	
	n=len(p[2][0])
	print "first character is string of length"
	print n
	if type(p[2][1])==str:
		q=len(p[2][1])
		print "second character is string of length"
		print q
		if type(p[2][2])==str:
			e=len(p[2][2])
			print "third character is string of length"
			print e
			if type(p[2][3])==str:
				s=len(p[2][3])
				print "fourth character is string of length"
				print s
	else :
		if type(p[2][2])==str:
			e=len(p[2][2])
			print "third character is string of length"
			print e
			if type(p[2][3])==str:
				s=len(p[2][3])
				print "fourth character is string of length"
				print s
		else :	
			if type(p[2][3])==str:
				s=len(p[2][3])
				print "fourth character is string of length"
				print s
elif type(p[2][1])==str:
	m=len(p[2][1])
	print "second character is string of length"
	print m
	if type(p[2][2])==str:
			e=len(p[2][2])
			print "third character is string of length"
			print e
			if type(p[2][3])==str:
				s=len(p[2][3])
				print "fourth character is string of length"
				print s
	else :	
		if type(p[2][3])==str:
			s=len(p[2][3])
			print "fourth character is string of length"
			print s
elif type(p[2][2])==str:
	l= len(p[2][2])
	print "third character is string of length"
	print l
	if type(p[2][3])==str:
		s=len(p[2][3])
		print "fourth character is string of length"
		print s
	
elif type(p[2][3])==str:
	print "fourth character is string of length"
	r=len(p[2][3])
	print r
else :
	print "no string"
	

