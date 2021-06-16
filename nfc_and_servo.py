#Libraries
import RPi.GPIO as GPIO
import os, time

started = time.time()

#GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT) #Pin 11 (BCM GPIO 17 on the raspberry pi)

#Positions
left=2
center=7
right=12

#Initialization
pwm=GPIO.PWM(11,50)
pwm.start(0)

#Actions
def open():
	pwm.ChangeDutyCycle(left) # Left - 90 deg position
	time.sleep(1)

def close():
	pwm.ChangeDutyCycle(right) # Right +90 position
	time.sleep(1)

def badge_to_int(b):
	if b == -1:
		return None
	return int(b.replace(' ', ''), base=16)

def reader():
	readnfc = os.popen("nfc-list").read()
	uidLoc = 'UID (NFCID1):'
	indexNFC = readnfc.find(uidLoc)
	badge=-1
	if indexNFC != -1:
		badge=readnfc[indexNFC+len(uidLoc):indexNFC+len(uidLoc)+15].strip(" ")
	print(badge_to_int(badge))
	return badge

badge = reader()
while(badge == -1):
	badge = reader()
	time.sleep(0.5)
	if(time.time() - started > 10):
		exit()
if(badge!=-1): #Add SSH servor request to check the authorization of the badge
	open()
	print('Authorized. Locker opened') 
input('Press Enter to close the locker')
close()

pwm.stop()
GPIO.cleanup()
