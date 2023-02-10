from tkinter import *
import tkinter as tk
import pygame 
from pygame import mixer
from tkinter import filedialog
#importations des libraries python mixer, filedialog, et pygame
#Filedialog permet d'importers des fichiers dans ton programme
#pygame permet d'importer le module mixer et d'autres sous-librairies
#mixer permet de jouer des musiqueq dans notres programme

#Initialisation du module mixer
mixer.init()

#Fonction qui permet de jouer une musique dans notre programme
#Grâce à une listbox, quand cette listbox est active, alors la musique se charge et se lance
def Playermusic():
    fichier = list_box.get(ACTIVE)
    mixer.music.load(fichier)
    mixer.music.play()
    
#Fonction qui permet de stopper la musique en cours d'éxecution
def Playermusic_stop():
    mixer.music.stop()

#Fonction permettant de mettre en pause la musique en cours
def pause():
    mixer.music.pause()

#Fonction permettant de remettre en route une musique en cours
def Unpause():
    mixer.music.unpause()

#Fonction permettant de définir la durée d'une musique
#Avec le paramètre "son", je définis mon volume  divisé sur 100
def Volume(son):
    mixer.music.set_volume(int(son)/100)

#Permet l'importation d'un fichier dans une listbox
#Grâce à la variable "fichier", je lui assigne la propriété permettant l'important de fichier type "mp3"
#Ensuite je l'insert dans ma listbox
def importation():
    global fichier
    fichier = filedialog.askopenfilename(filetypes=(("Mp3 Files", "*.mp3"),))
    list_box.insert(END,fichier)

#Permet de supprimer  des éléments de ma listbox
def supprime():
    list_box.delete(ANCHOR)

#Permet de jouer à nouveaux une musique à l'infini
#Grâce à ma loops-1 je recommence la musique du début
def loop():
    fichier = list_box.get(ACTIVE)
    mixer.music.load(fichier)
    mixer.music.play(loops=-1)

#Interface utilisateur
root = tk.Tk()
root.title("playerMusic")
root.configure(background="dark blue")
root.geometry("500x400")

#Fenêtre musicPlayer
interface = Label(root,text="",relief="raised",width=50,height=17)
interface.pack(expand=True,fill=X)
interface.place(x=50,y=70)

#Boutton MusicPlayer
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
boutton_5 = Button(root,text="Import",command=importation,relief="raised")
boutton_5.pack()
boutton_5.place(x=270,y=330)
boutton_6 = Button(root,text="Supprimer",command=supprime,relief="raised")
boutton_6.pack()
boutton_6.place(x=170,y=330)
boutton_7 = Button(root,text="reload",command=loop,relief="raised")
boutton_7.pack()
boutton_7.place(x=270,y=300)

#Double variable pour le volume
volume = tk.DoubleVar()

#Volume de musique, de 0 à 100
scale = tk.Scale(root,orient='vertical', from_=0,to=100,command=Volume)
scale.pack()
scale.place(x=50,y=160)

#List_box pour la sélection de la musique
list_box = Listbox(root)
list_box.pack()
list_box.place(x=120,y=90)

root.mainloop()