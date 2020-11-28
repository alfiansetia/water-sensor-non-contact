#Libraries
import RPi.GPIO as GPIO
import sys
import telepot
import time
#IMPORT LIBRARY OS
import os 
import telepot


text = 'AIR HABIS'
text1 = 'AIR TERSEDIA'
chat_id = CHATID

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numberi

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
if GPIO.input(15) != GPIO.LOW :
    bot = telepot.Bot('TOKEN')
    bot.sendMessage(chat_id, text)
else :
    bot = telepot.Bot('TOKEN')
    bot.sendMessage(chat_id, text1)
