import os
import random
import time


import playsound
import speech_recognition as sr
from time import ctime
import webbrowser

from gtts import gTTS

r = sr.Recognizer()
def record_audio(ask = False):
  with sr.Microphone() as source:
    # print('say source')
    if ask :
        kp_speak(ask)
    audio=r.listen(source)
    voice_data = ''
    try:
     voice_data=r.recognize_google(audio)
    # print(voice_data)
    except sr.UnknownValueError:
        kp_speak('sorry, i did not get you')
    except sr.RequestError:
        kp_speak('sorry my speech service is down')
    return voice_data


def kp_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r =random.randint(1,10000000)
    audio_file ='audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        kp_speak('My name is alexa')
    if 'what is current time' in voice_data:
        kp_speak('time is '+ctime())
    if 'what you do' in voice_data:
        kp_speak('i help you to search')
    if 'who developed you' in voice_data:
        kp_speak('komal patil devloped me')
    if 'search' in voice_data:
        search =record_audio('what you want to serach for? ')
        url ='https://google.com/search?q='+ search
        webbrowser.get().open(url)
        kp_speak('here what i found' + search)
    if 'open dictionary' in voice_data:
        word=record_audio('tell me word')
        url ='https://google.com/search?q='+ word
        webbrowser.get().open(url)
        kp_speak('here what i found'+word)
    if 'find location' in voice_data:
        location = record_audio('what is the location? ')
        url ='https://google.com/maps/place/'+ location + '/&amp'
        webbrowser.get().open(url)
        kp_speak('here what i found' + location)
    if ('exit alexa' or 'bye alexa') in voice_data:
        kp_speak('bye... take care ... have a nice day')
        exit()

time.sleep(1)

kp_speak('how can i help you?')
while 1:
 voice_data = record_audio()
 respond(voice_data)
