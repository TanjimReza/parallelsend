import pyautogui
import time
import datetime
import os
import sys
os.system("title Parallel Send - Tanjim Reza")
os.system("MODE 74,30")
#========================================== Kapshi ==========================================================#
CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 
#========================================= Main Class =======================================================#
class Spammer:
	classLoop = 0
	totalSent = 0
	def __init__(self,loop,msgs):
		self.loop = loop
		self.msgs = msgs
		Spammer.classLoop = loop


	def indefinite():
		while True:
			Spammer.sender()

	def definite():
		for i in range(Spammer.classLoop):
			Spammer.sender()


	def sender():
		#=========== Log ===========#
		print("Total Sent:",Spammer.totalSent)
		secondCount = 0
		for seconds in range(waitTime):
			#=========== Log ===========#
			print("Waiting: "+ str(secondCount) + " seconds")
			#=========== Waiting Time ===========# 
			time.sleep(1)
			#=========== Overwriting Previous Log v1 ===========#
			sys.stdout.write(CURSOR_UP_ONE) 
			sys.stdout.write(ERASE_LINE)
			secondCount += 1
		#============= Writing the Actual Message ============#
		for msgs in messageStore:
			pyautogui.typewrite(msgs)
			pyautogui.press("enter")
		#=========== Overwriting Previous Log v2 ===========#
		sys.stdout.write(CURSOR_UP_ONE) 
		sys.stdout.write(ERASE_LINE)  
		Spammer.totalSent += 1 #take to last 

#========================================= Welcome Message ======================================================#

print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ")
print("::::::::::::::::::::::: Welcome to Message Spammer ::::::::::::::::::::::: ")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
print("Customize & Send Automatic Messages of Comment.\nNote:Point your cursor to message box to start sending.")
print("-------------------------------- Start ----------------------------------\n\n")

#============================= How mane times should the program run ============================#
while True:
	try:
		loopCount = int(input("How many times do you want to write?(For unlimited enter 0)\n="))
		n = 0  
		if loopCount is n:
			systemRun = True
		else:
			systemRun = int(loopCount)
		break
	except:
		print("Error: Input must be Digits!")
#=====================================  Messages per turn  ======================================#
while True:
	try:
		messageCount = int(input("How many different messages at once?\n="))
		break
	except:
		print("Error: Input must be Digits!")

print("Type each message in one line & press enter-\n===============================")
messageStore = []
for i in range(messageCount):
	messageStore.append(input())
print("===============================")
#===================================== Watiting time per message =================================#

waitTime = int(input("Waiting time for each message(seconds)?="))

#=====================================    Calling the Sender    =================================#
for i in range(3):
	print("Starting in ",i, end="\r")

print("Started: ",datetime.datetime.now().strftime("%I:%M:%S-%B,%Y")) 

Spammer(loop=systemRun,msgs=messageStore)
Spammer.definite()


print("Total Sent:", Spammer.totalSent)
print("Ended: ",datetime.datetime.now().strftime("%I:%M:%S-%B,%Y")) 
