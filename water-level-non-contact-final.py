#Libraries
import RPi.GPIO as GPIO
import sys
import telepot
import time
#IMPORT LIBRARY OS
import os 
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

 
def distance():
    #set GPIO Pins
    GPIO.setmode(GPIO.BCM)
    GPIO_TRIGGER = 18
    GPIO_ECHO = 24
     
    #set GPIO direction (IN / OUT)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def water():
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BCM) # Use physical pin numbering
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    # if GPIO.input(15) != GPIO.LOW:
    #     status = "habis"
    #     # bot.sendMessage(chat_id, text)
    #     # print("Button was pushed!")
    # else:
    #     status = "penuh"
    #     # print("Im stanby")


def telegram(mode):
    text = 'AIR HABIS'
    text1 = 'AIR TERSEDIA'
    chat_id = 'YOUR CHAT ID'
    bot = telepot.Bot('YOUR BOT')
    if mode == "habis":
        bot.sendMessage(chat_id, text)
        # print("Button was pushed!")
    elif mode == "penuh":
        bot.sendMessage(chat_id, text1)
        # print("Im stanby")
    else :
        bot.sendMessage(chat_id, "PERINTAH TIDAK DIKETAHUI")



def pump(mode):
    pin = 4
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    if mode == "on" :
        GPIO.output(pin, GPIO.HIGH)
        # time.sleep(2)
        GPIO.output(pin, GPIO.LOW)
        # time.sleep(2)
    elif mode == "off" :
        GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()
    else :
        print("PERINTAH TIDAK DIKETAHUI")
        GPIO.cleanup()



if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            water()
            time.sleep(0.3)
            if GPIO.input(15) != GPIO.LOW : 
                telegram("habis")
            else :
                #IF TRUE JIKA DISTANCE KURANG DARI 17 MAKA EKS FILE SERVO DAN LAMPU
                if dist < 5 :
                    pump("on")
                    telegram("penuh")
                    # print("HIDUP")
                    # os.system('python /path/servo.py')
                    # os.system('python on1.py')
                #ELSE MEMATIKAN LAMPU
                else :
                    pump("off")
                    # print("MATI")
                    # os.system('python off1.py')
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        pump('off')
        GPIO.cleanup()
        print("Measurement stopped by User")
        