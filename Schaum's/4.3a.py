#!/usr/bin/python

#all pair of elements whose sum is 25


import numpy as np

A = np.arange(25).reshape(5,5)

print A

i=0
while i <= 4 :
	for j in range(5):
		k=4
		while k != j :
			sum = A[i][j] + A[i][k]
			if sum == 25 :
				print A[i][j] , A[i][k]
				break
			else :
				k -= 1

	i += 1 
