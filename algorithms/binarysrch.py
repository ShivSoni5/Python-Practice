#!/usr/bin/python

a=list(input("Enter the sorted array from which you want to search : "))

key=input("Enter the number you want to search: ")

n=len(a)

def Bnysch(a,l,r,key):
	if r >= l:
		mid = l+ (r-l)/2

		if key==a[mid]:
			return mid

		elif key<a[mid]:
			return Bnysch(a,l,mid-1,key)

		else :
			return Bnysch(a,mid+1,r,key)

	else :
		return -1

result=Bnysch(a,0,n-1,key)

if result != -1: 
	print("your key is present at "+ str(result))

else:
	print("key nary search is not present")
