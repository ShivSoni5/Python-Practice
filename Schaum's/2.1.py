#!/usr/bin/python2

def DIV(J,K):
    if K % J == 0:
        print 1

    else :
        print 0


m=int(raw_input("Enter Divisor : "))
n=int(raw_input("Enter Divident : "))

DIV(m,n)
