#!/usr/bin/python2

#ALARM	


import subprocess,time

Date=raw_input("Enter the date in format YYYY:MM:DD or press return for today: ")
Time=raw_input("Enter the time in format HH:MM(should be in 24-hr format): ")


dt=list(time.localtime())
print dt
print Time[0:2] 
print Time[3:5] 

def alarm():
        sound_prgrm= "/usr/bin/cvlc" #place the path to player here
        sound_file="Melody" #alarm tone
        subprocess.call([sound_prgrm, sound_file])


while True:
	dt=list(time.localtime())
	if Date=="":
		if dt[3]==int(Time[0:2]) and dt[4]==int(Time[3:5]):
			print("hi")			
			alarm()
	
	elif dt[0]==int(Date[0:4]) and dt[1]==int(Date[5:7]) and dt[2]==int(Date[8:]) and dt[3]==int(Time[0:2]) and dt[4]==int(Time[3:5]) :
		alarm()


