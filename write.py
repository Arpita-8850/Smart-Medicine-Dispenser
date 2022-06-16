import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

read = SimpleMFRC522()

try:
	txt = input('new data:')
	print("Your tag")
	read.write(txt)
	print("written").w
finally:
	GPIO.cleanup()
