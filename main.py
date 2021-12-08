import os
from dotenv import load_dotenv
load_dotenv()  
API_KEY=os.getenv("Wolfram_API_KEY")
import wolframalpha
client = wolframalpha.Client(API_KEY)

import wikipedia
import PySimpleGUI as sg 

sg.theme('DarkRed')  
layout = [  [sg.Text('Enter a command'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window('Virtual Assistant', layout)
import pyttsx3
engine = pyttsx3.init()

while True:
    event, values = window.read()
    if event in (None,'Cancel'): # if user closes window or clicks cancel
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking('Wolfram Result: '+wolfram_res,'Wikipedia Result: '+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)


    # engine.say(wiki_res)
    engine.runAndWait()

    print(values[0])


window.close()