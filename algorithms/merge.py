#!/usr/bin/python

def merge(A,p,q,r):
	n1 = q - p + 1
	n2 = r -q

	L = [0] * n1
	R = [0] * n2

	for i in range(0,n1) :
		L[i] = A[p+i]

	for j in range(0,n2) :	
		R[j] = A[q+1+j]

	i=0
	j=0
	k=p

	while i < n1 and j < n2:
		if L[i] <=  R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
		k += 1

	while i < n1 :
		A[k] = L[i]
		i += 1
		k += 1

	while j < n2 :
		A[k] = R[j]
		j += 1
		k += 1


def mergesort(A,l,r):
	if l < r:
		m = (l+(r-1))/2
		mergesort(A,l,m)	
		mergesort(A,m+1,r)
		merge(A,l,m,r)

A=list(input("Enter the list you want to get sorted: "))
n=len(A)


mergesort(A,0,n-1)

print A
