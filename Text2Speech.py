from typing import Text
import pyttsx3
import os

def checking():
    while True:
        inputing1 = input("Check The File? : ")
        if (inputing1 == "Y") or (inputing1 == "y") : 
            os.startfile("text.txt")
            break
        if (inputing1 == "N") or (inputing1 == "n") :
            break

def reading():
    while True:
        inputing2 = input("Read The File? : ")
        if (inputing2 == "Y") or (inputing2 == "y") : 
            engine. say(text.read())
            break
        if (inputing2 == "N") or (inputing2 == "n") :
            break

try:
    engine = pyttsx3. init()
    text = open("text.txt", "r")

    voices = engine. getProperty('voices')

    engine. setProperty('voice', voices[2]. id) #changing index changes voices but ony 0 and 1 and 2 are working here.

    checking()
    reading()

    engine. runAndWait()
finally:
    text.close()