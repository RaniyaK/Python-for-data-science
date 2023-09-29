from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox  
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo
from googletrans import Translator,LANGUAGES
from io import BytesIO 
from gtts import gTTS
from playsound import playsound
import tkinter as tk
import pyttsx3
import speech_recognition as sr
import pygame
import time
import os
 
pygame.init()
pygame.mixer.init()
root = Tk()
root.title("DRapps voice/text translator")
root.geometry('700x600')
root.resizable(0,0)
root.configure(bg = "#F7AC40")
drapp_logo = PhotoImage(file = r"C:\Users\computer lab\Desktop\python\DRapps.png")

Label(root, image = drapp_logo ,bg = "#F7AC40").place(x=598, y=550)

root.iconbitmap(r'C:\Users\computer lab\Desktop\python\DRapps.ico')


def wait():
    while pygame.mixer.get_busy():
        time.sleep(.1)

def Translate():
    translator = Translator()
    translated = translator.translate(text=text_box.get(),dest=dest_lang.get())
    output_text.delete(1.0,END)
    output_text.insert(END,translated.text)

tts = pyttsx3.init()

def speak():
    global output_text
    mp3_fo = BytesIO()
    tts = gTTS(output_text.get(0.0, tk.END), lang=dest_lang.get())
    tts.write_to_fp(mp3_fo)
    mp3_fo.seek(0)
    sound = pygame.mixer.Sound(mp3_fo)
    sound.play()
    wait()

def speakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def record():
    global text1
    r = sr.Recognizer()
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2,duration=1)
        speakText("speak now")
        audio2 = r.listen(source2,timeout=1)
        try:
            text1 = r.recognize_google(audio2,language = str(input_lang.get()))
            print(text1)
            newtext.delete(1.0,END)
            newtext.insert(END,text1)
        except Exception as ex:
            print(ex)

def Translate():
    translator = Translator()
    translated = translator.translate(text=text_box.get(),dest=dest_lang.get())
    output_text.delete(1.0,END)
    output_text.insert(END,translated.text)

def Translate1():
    translator = Translator()
    translated = translator.translate(text=newtext.get(1.0,END),dest=dest_lang.get())
    output_text.delete(1.0,END)
    output_text.insert(END,translated.text)

language = list(LANGUAGES.keys())
dest_lang = ttk.Combobox(root,values = language, width = 22)
dest_lang.place(x=30,y=370)
dest_lang.set('choose language')

input_lang = ttk.Combobox(root,values = language, width = 22)
input_lang.place(x=30,y=145)
input_lang.set('choose language')
    

upper_frame = Frame(root,bg="#14A7DD",width = 900,height = 130)
upper_frame.place(x=0,y=0)

picture = PhotoImage(file = r"C:\Users\computer lab\Desktop\python\voice.png")
Label(upper_frame,image = picture,bg = "#14A7DD").place(x=50,y=12)
Label(upper_frame,text = "My Translator",font = "TimesNewRoman 40 bold",bg = "#14A7DD",fg = 'white').place(x=240,y=30)


newtext = Text(root, font=12, height=4, width=37)
newtext.place(x=200, y=145)

trans_btn1 = Button(root,text = 'Translate Audio', font = 'Arial 12 bold',borderwidth='0.1c',width = 13, command = Translate1, bg = 'Pink',activebackground = 'green' )
trans_btn1.place (x=550,y=160)

Label(root,text = "Text to be translated", font = "Arial 13 bold", bg = '#F7AC40').place(x=30,y=240)
text_box = Entry(root,font="calibri 13",width=56)
text_box.place(x=30,y=260,height=100)



Label(root,text = "Output", font = "Arial 13 bold", bg = '#F7AC40').place(x=30,y=390)
output_text = Text(root,font = "Arial 13 bold", height = 5,wrap = WORD, padx = 5, pady= 5, width = 55)
output_text.place(x=30,y=420)

trans_btn = Button(root,text = 'Translate Text', font = 'Arial 12 bold',borderwidth='0.1c', width = 13, command = Translate, bg = 'Pink',activebackground = 'green' )
trans_btn.place (x=550,y=280)



play_button = PhotoImage(file = r"C:\Users\computer lab\Desktop\python\play.png")
play_btn = Button(root,text = "play", compound = LEFT, image = play_button,bg = 'white', width = 130, font = "arial 14 bold", borderwidth='0.1c', command = speak)
play_btn.place(x=550,y=430)

rec_button = PhotoImage(file = r"C:\Users\computer lab\Desktop\python\rec.png")
rec_btn = Button(root,image = rec_button, bg = 'white', font = "arial 12 bold", borderwidth='0.1c', command = lambda : record() )
rec_btn.place(x=30,y=175)


root.mainloop()