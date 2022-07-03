from cProfile import label
from turtle import width
from pygame import mixer
from tkinter import Label
from tkinter import Tk
from tkinter import Button
from tkinter import filedialog
from tkinter import font

CurrentVolume = 0.5

#Functions
def PlaySong():
    filename=filedialog.askopenfilename(initialdir="C:\\Users\\kulka\\Music",title="Select a song")
    print(filename)
    try:
        mixer.init()
        mixer.music.load(filename)
        mixer.music.play()
        volumelabel.config(fg="green",text="Volume: "+str(CurrentVolume))
    except Exception as e:
        print(e)
        songtitle_label.config(fg="blue",text="Error playing the music")
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

#Buttons:
Button(main,text = "Select song",font=("Calibri",10),command=PlaySong).grid(sticky="N",row=2)
Button(main,text = "Pause",font=("Calibri",10),command=pause).grid(sticky="W",row=3)
Button(main,text = "Resume",font=("Calibri",10),command=resume).grid(sticky="E",row=3)
Button(main,text = "Up",font=("Calibri",10),width=5,command=volumeup).grid(sticky="W",row=5)
Button(main,text = "Down",font=("Calibri",10),width=5,command=volumedown).grid(sticky="E",row=5)
#mainloop tells python to run tkinter
main.mainloop()
