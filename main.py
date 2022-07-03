from cProfile import label
from turtle import width
from pygame import mixer
from tkinter import Label
from tkinter import Tk
from tkinter import Button
from tkinter import filedialog
from tkinter import font

def volumedown():
    try:
        global CurrentVolume
        if CurrentVolume <= 0:
            volumelabel.config(fg="blue",text="Volume : Muted")
            return
        CurrentVolume=CurrentVolume-float(0.25)
        mixer.music.set_volume(CurrentVolume)
    except Exception as e:
        print(e)
        songtitle_label.config(fg="blue",text="Please select a file first")

def volumeup():
    try:
        global CurrentVolume
        if CurrentVolume>=1:
            volumelabel.config(fg="blue",text="Volume : Max")
            return
        CurrentVolume=CurrentVolume+float(0.25)
        mixer.music.set_volume(CurrentVolume)
    except Exception as e:
        print(e)
        songtitle_label.config(fg="blue",text="Please select a file first")

def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        songtitle_label.config(fg="blue",text="Please select a track first")

def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        songtitle_label.config(fg="blue",text="Please select a track first")

main = Tk()
main.title("Python Mini Project")
#Labels in the widget window
Label(main,text = "MP3 Music Player",font=("Calibri",15),fg="red").grid(sticky="N",padx=120,row = 0)
Label(main,text="Select song you want to play",font=("Calibri",10),fg="green").grid(sticky="N",row=1)
songtitle_label = Label(main,font=("Calibri",10))
songtitle_label.grid(sticky="N",row = 3)
Label(main,text="Volume",font=("Calibri",10),fg="green").grid(sticky="N",row=4)
volumelabel = Label(main,font=("Calibri",10))
volumelabel.grid(sticky="N",row = 5)

main.mainloop()
