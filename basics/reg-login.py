#!/usr/bin/python2

from time import ctime
import commands as cmd

print """
__________________________________

Welcome to our site..
____________________________________


You want to login or register?

Press 'l' for LOGIN and 'r' for REGISTER

___________________________________


"""
x=raw_input("Login or Register:")

def reg():
        f=open("register","a")
        u=raw_input("Enter username:")
        n=cmd.getoutput("wc -l < register")
        x=int(n)
        for i in range(x+1):    #(x+1) is used because for the first registration i will be zero and then the "head -0 "
                c=cmd.getoutput("awk -F : '{print $1}' register | grep "+u+" | head -"+str(i)+" | tail -1 ")
	if c==u:
        	print "username already exist"
        else:
		p=raw_input("Enter password:")
                f.write(""+u+":"+p+"\n")
		print "successfully registered"
	f.close()

if x=="r":
	reg()


def login():
	u=0
	while u<3:
		n=raw_input("Enter username:")
		global n
		k=cmd.getoutput("awk -F : '{print $1}' register | grep "+n+"")
		if k==n:
	  		pwd(""+n+"",0)
		       	break
		else:
			print"Username not found!"
			if u==2:
				print"it seems you are not registered..try to register here"
				reg()
		u=u+1



def pwd(e,z):
	while z<3:
		q=raw_input("Enter password:")
		r=cmd.getoutput("cat register | grep "+e+":"+q+" > logs")
		s=cmd.getoutput("awk -F : '{print $2}' logs | grep "+q+"")
		if s==q:
			print "successfully logged in!!"
		        t=ctime()
			f=open("login","w")
		        f.write(""+e+" login at "+t+"\n")
		        f.close()
			break
		 
		else:
		
			print "Incorrect password!! Try again"
			print z
			z=z+1			
			pwd(n,z)
			if z==2:
				print"Try after some time."
				break
			break		
		
		
              	break	 

				
if x=="l":
	login()
		

	
	  	
	
