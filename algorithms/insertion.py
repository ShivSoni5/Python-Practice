#!/usr/bin/python

A=list(input("Enter the numbers (separated by ',') to be sorted: "))
 

print "Sort in NonDecreasing order - press 1\n"
print "Sort in NonIncreasing order - press 2\n\n"
C=raw_input("Enter your choice: ")
print "\n\n"
print "Before sorting : "+str(A)


def ND(A):
	for j in range(1,len(A)):
		key=A[j]
		i=j-1
		while i>=0 and key < A[i] :
			A[i+1]=A[i]
			i=i-1
		A[i+1]=key

def NI(A):
	for j in range(1,len(A)):
                key=A[j]
                i=j-1
                while i>=0 and key > A[i] :
                        A[i+1]=A[i]
                        i=i-1
                A[i+1]=key

if C == "1":
	ND(A)
else:
	NI(A)
 
print "After sorting : "+str(A)

