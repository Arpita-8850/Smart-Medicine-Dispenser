# import RPi.GPIO as GPIO
# from mfrc522 import SimpleMFRC522

# rfid = SimpleMFRC522()

def readUserId():
    try:
        print("Place tag")
        # text = rfid.read()
        text = 1
        # print(text)
        return(text)

    finally:
        pass
        # GPIO.cleanup()