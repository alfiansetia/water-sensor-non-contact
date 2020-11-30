#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
mode = 'on'
pin = 4
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)
if mode == "on" :
     GPIO.output(pin, GPIO.HIGH)
     GPIO.output(pin, GPIO.LOW)
elif mode == "off" :
     GPIO.output(pin, GPIO.LOW)
     GPIO.cleanup()
else :
     print("PERINTAH TIDAK DIKETAHUI")
     GPIO.cleanup()
