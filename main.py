import speech_recognition as sr
import os
import pyaudio 
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM 
import youtube_dl 
#import vlc 
import urllib3
from gtts import gTTS
import playsound
import json
from bs4 import BeautifulSoup as soup
import urllib3 
import wikipedia
import random
from time import strftime

                                        
def peppersaythis(text):
	r1 = random.randint(1,10000000)
	r2 = random.randint(1,10000000)
	filename = str(r2)+"audio"+str(r1)+".mp3"
	tts = gTTS(text = text , lang = "en-in")
	tts.save(filename)
	playsound.playsound(filename)
	os.remove(filename)


def mycommand():                           # obtain audio from the microphone
	r = sr.Recognizer()
	r.energy_threshold = 2200
	r.dynamic_energy_threshold = True
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

	try:
		said= r.recognize_google(audio)	
		print("you said: " + said + "\n")
		#in case the speech is unrecognizable
	except Exception as e :
			print("exception" + str(e))
			said= mycommand()
	return said.lower()
                     


def assistant(command):
	if command in ["stop","terminate"]:
		peppersaythis("okay")
		sys.close()


peppersaythis("hello, what can i do for you akshay!")

while(True):
	assistant(mycommand())
