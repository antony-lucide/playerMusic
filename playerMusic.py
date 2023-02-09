from tkinter import *
import tkinter as tk
import pygame 
from pygame import mixer
from tkinter import filedialog



mixer.init()

def Playermusic():
    fichier = list_box.get(ACTIVE)
    mixer.music.load(fichier)
    mixer.music.play()
    

def Playermusic_stop():
    mixer.music.stop()

def pause():
    mixer.music.pause()


def Unpause():
    mixer.music.unpause()

def Volume(son):
    mixer.music.set_volume(int(son)/100)

def importation():
    global fichier
    fichier = filedialog.askopenfilename(filetypes=(("Mp3 Files", "*.mp3"),))
    list_box.insert(END,fichier)

def supprime():
    list_box.delete(ANCHOR)


def loop():
    fichier = list_box.get(ACTIVE)
    mixer.music.load(fichier)
    mixer.music.play(loops=-1)


root = tk.Tk()
root.title("playerMusic")
root.configure(background="dark blue")
root.geometry("600x400")
interface = Label(root,text="Music",relief="raised",width=50,height=17)
interface.pack(expand=True,fill=X)
interface.place(x=50,y=70)
boutton =  Button(root,text="Play",command=Playermusic,relief="raised")
boutton.pack()
boutton.place(x=70,y=300)
boutton_2 = Button(root,text="stop",command=Playermusic_stop,relief="raised")
boutton_2.pack()
boutton_2.place(x=130,y=300)
boutton_3 = Button(root,text="Pause",command=pause,relief="raised")
boutton_3.pack()
boutton_3.place(x=200,y=300)
button_4 = Button(root,text="Unpause",command=Unpause,relief="raised")
button_4.pack()
button_4.place(x=69,y=330)
volume = tk.DoubleVar()
scale = tk.Scale(root,orient='vertical', from_=0,to=100,command=Volume)
scale.pack()
scale.place(x=50,y=160)
boutton_5 = Button(root,text="Import",command=importation,relief="raised")
boutton_5.pack()
boutton_5.place(x=200,y=90)
list_box = Listbox(root)
list_box.pack()
list_box.place(x=290,y=90)
boutton_6 = Button(root,text="Supprimer",command=supprime,relief="raised")
boutton_6.pack()
boutton_6.place(x=300,y=275)
boutton_7 = Button(root,text="reload",command=loop,relief="raised")
boutton_7.pack()
boutton_7.place(x=300,y=310)
root.mainloop()