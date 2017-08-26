#!/usr/bin/python

a=list(input("Enter the sorted array from which you want to search : "))

key=input("Enter the number you want to search: ")

n=len(a)

def Bnysch(a,n):
	if key==a[n/2]:
		print ("key present at location "+str((n/2)+1) )

	elif key<a[n/2]:
		Bnysch(a,n/2)

	else:
		Bnysch(n/2+1,n)

Bnysch(a,n)
