# coding: utf8
from mingus.midi import fluidsynth
import time
from random import randint
import Tkinter
import tkMessageBox

fluidsynth.init('/usr/share/sounds/sf2/FluidR3_GM.sf2',"alsa")


#  dictionary for interval names
intervals = {  1 : "kleine Sekunde", \
2 : "große Sekunde" , \
3 : "kleine Terz" , \
4 : "große Terz" , \
5 : "Quart" , \
6 : "Tritonus" , \
7 : "Quinte" , \
8 : "kleine Sexte" , \
9 : "große Sexte" , \
10 : "kleine Septime" , \
11 : "große Septime" , \
12 : "Oktave" , \
13 : "Oktave + kleine Sekunde" , \
14 : "Oktave + große Sekunde" , \
15 : "Oktave + kleine Terz" , \
16 : "Oktave + große Terz" , \
17 : "Oktave + Quart" , \
18 : "Oktave + Tritonus" , \
19 : "Oktave + Quinte" , \
20 : "Oktave + kleine Sexte" , \
21 : "Oktave + große Sexte" , \
22 : "Oktave + kleine Septime" , \
23 : "Oktave + große Septime" , \
24 : "2 Oktaven" }

chords_3_notes =[[0,4,7],#Dur Grundstellung
                [0,3,8],#Dur Sextakkord
                [0,5,9],#Dur Quartsextakkord
                [0,3,7],#Moll Grundstellung
                [0,4,9],#Moll Sextakkord
                [0,5,8],#Moll Quartsextakkord
                [0,3,6],#vermindert Grundstellung
                [0,3,9],#vermindert Sextakkord
                [0,6,9],#vermindert Quartsextakkord
                [0,4,8]]#übermäßig

chords_3_names = ["Dur Grundstellung",
                "Dur Sextakkord",
                "Dur Quartsextakkord",
                "Moll Grundstellung",
                "Moll Sextakkord",
                "Moll Quartsextakkord",
                "vermindert Grundstellung",
                "vermindert Sextakkord",
                "vermindert Quartsextakkord",
                "übermäßig"]

chords_4_notes = [[0,4,7,12], #Dur Grundstellung
                  [0,3,8,12], #Dur Sextakkord
                  [0,5,9,12], #Dur Quartsextakkord
                  [0,3,7,12], #Moll Grundstellung
                  [0,4,9,12], #Moll Sextakkord
                  [0,5,8,12], #Moll Quartsextakkord
                  [0,4,7,10], #Dur kleiner Septakkord, Grundstellung
                  [0,3,6,8], #Dur kleiner Septakkord, Quintsextakkord
                  [0,3,5,9], #Dur kleiner Septakkord, Terzquartakkord
                  [0,2,6,9], #Dur kleiner Septakkord, Sekundakkord
                  [0,3,7,10], #Moll kleiner Septakkord, Grundstellung
                  [0,4,7,9], #Moll kleiner Septakkord, Quintsextakkord
                  [0,3,5,8], #Moll kleiner Septakkord, Terzquartakkord
                  [0,2,5,9], #Moll kleiner Septakkord, Sekundakkord
                  [0,4,7,11], #Dur großer Septakkord, Grundstellung
                  [0,3,7,8], #Dur großer Septakkord, Quintsextakkord
                  [0,4,5,9], #Dur großer Septakkord, Terzquartakkord
                  [0,1,5,8], #Dur großer Septakkord, Sekundakkord
                  [0,3,7,11], #Moll großer Septakkord, Grundstellung
                  [0,4,7,8], #Moll großer Septakkord, Quintsextakkord
                  [0,4,5,8], #Moll kleiner Septakkord, Terzquartakkord
                  [0,1,4,8], #Moll großer Septakkord, Sekundakkord
                  [0,4,7,9], #Dur Sixtajoutee Grundstellung
                #   [0,3,5,8], #Dur Sixtajoutee 1. Umkehrung
                #   [0,2,6,9], #Dur Sixtajoutee 2. Umkehrung
                #   [0,3,7,10], #Dur Sixtajoutee 3. Umkehrung
                  [0,3,7,9], #Moll Sixtajoutee Grundstellung
                #   [0,4,6,9], #Moll Sixtajoutee 1. Umkehrung
                #   [0,2,5,8], #Moll Sixtajoutee 2. Umkehrung
                #   [0,3,6,10], #Moll Sixtajoutee 3. Umkehrung
                  [0,3,6,10], #Halbvermindert
                  [0,3,6,9]] #Ganzvermindert



chords_4_names = ["Dur Grundstellung",
                  "Dur Sextakkord",
                  "Dur Quartsextakkord",
                  "Moll Grundstellung",
                  "Moll Sextakkord",
                  "Moll Quartsextakkord",
                  "Dur kleiner Septakkord, Grundstellung",
                  "Dur kleiner Septakkord, Quintsextakkord",
                  "Dur kleiner Septakkord, Terzquartakkord",
                  "Dur kleiner Septakkord, Sekundakkord",
                  "Dur großer Septakkord, Grundstellung",
                  "Dur großer Septakkord, Quintsextakkord",
                  "Dur großer Septakkord, Terzquartakkord",
                  "Dur großer Septakkord, Sekundakkord",
                  "Moll kleiner Septakkord, Grundstellung",
                  "Moll kleiner Septakkord, Quintsextakkord",
                  "Moll kleiner Septakkord, Terzquartakkord",
                  "Moll kleiner Septakkord, Sekundakkord",
                  "Moll großer Septakkord, Grundstellung",
                  "Moll großer Septakkord, Quintsextakkord",
                  "Moll großer Septakkord, Terzquartakkord",
                  "Moll großer Septakkord, Sekundakkord",
                  "Dur Sixtajoutee Grundstellung",
                #   "Dur Sixtajoutee 1. Umkehrung",
                #   "Dur Sixtajoutee 2. Umkehrung",
                #   "Dur Sixtajoutee 3. Umkehrung",
                  "Moll Sixtajoutee Grundstellung",
                #   "Moll Sixtajoutee 1. Umkehrung",
                #   "Moll Sixtajoutee 2. Umkehrung",
                #   "Moll Sixtajoutee 3. Umkehrung",
                  "Halbvermindert",
                  "Ganzvermindert"
                  ]



def start_accords():

  i = 0
  base = 40
  for chord in chords_4_notes:
    tkMessageBox.showinfo(" ", "Spiele Vierklang " + chords_4_names[i] )
    for note in chord:
      fluidsynth.play_Note(note+base, 0,100)
      time.sleep(0.6)

    for note in chord:
      fluidsynth.play_Note(note+base, 0,100)
    time.sleep(1)
    i = i+1



def start_chord_3_training():

  while(True):
    base = randint(30,55)
    idx = randint(0,len(chords_3_names)-1)
    tkMessageBox.showinfo(" ", "Spiele Dreiklang!")
    chord = chords_3_notes[idx]

    for note in chord:
      fluidsynth.play_Note(note+base, 0,100)
    time.sleep(1)
    while(True):
      result = tkMessageBox.askquestion("", "Dreiklang erneut abspielen?", icon='warning')
      if result == 'yes':
        for note in chord:
          fluidsynth.play_Note(note+base, 0,100)
        time.sleep(1)
      else:
        tkMessageBox.showinfo(" ", "Zeige Lösung!")
        s =  chords_3_names[idx]
        tkMessageBox.showinfo("Die Antwort lautet: ", s)
        answer = tkMessageBox.askquestion("", "Zu Hauptmenü zurückkehren?", icon='warning')
        if answer == 'yes': return
        break



def start_chord_4_training():

  while(True):
    base = randint(30,55)
    idx = randint(0,len(chords_4_names)-1)
    tkMessageBox.showinfo(" ", "Spiele Vierklang!")
    chord = chords_4_notes[idx]

    for note in chord:
      if note == 0:
        print ('note == 0')
        fluidsynth.play_Note(note+base, 0,150)
      else:
        print ('note != 0')
        fluidsynth.play_Note(note+base, 0,100)
    time.sleep(1)
    while(True):
      result = tkMessageBox.askquestion("", "Vierklang erneut abspielen?", icon='warning')
      if result == 'yes':
        for note in chord:
          if note == 0:
            fluidsynth.play_Note(note+base, 0,150)
          else:
            fluidsynth.play_Note(note+base, 0,100)
        time.sleep(1)
      else:
        tkMessageBox.showinfo(" ", "Zeige Lösung!")
        s =  chords_4_names[idx]
        tkMessageBox.showinfo("Die Antwort lautet: ", s)
        answer = tkMessageBox.askquestion("", "Zu Hauptmenü zurückkehren?", icon='warning')
        if answer == 'yes': return
        break



def start_interval_training():

  while(True):
    lower = randint(30,55)
    upper = lower + randint(2,20)
    diff = upper - lower

    tkMessageBox.showinfo(" ", "Spiele Intervall!")
    fluidsynth.play_Note(lower,0,100)
    fluidsynth.play_Note(upper,0,100)
    time.sleep(1)
    while(True):
      result = tkMessageBox.askquestion("", "Intervall erneut abspielen?", icon='warning')
      if result == 'yes':
        fluidsynth.play_Note(lower,0,100)
        fluidsynth.play_Note(upper,0,100)
        time.sleep(1)
      else:
        tkMessageBox.showinfo(" ", "Zeige Lösung!")
        s =  str(intervals[diff]) + "\n" + str(diff) + " Halbtonschritte"
        tkMessageBox.showinfo("Die Antwort lautet: ", s)
        answer = tkMessageBox.askquestion("", "Zu Hauptmenü zurückkehren?", icon='warning')
        if answer == 'yes': return
        break


window = Tkinter.Tk()

B1 = Tkinter.Button(window, text ="Intervalltraining", command = start_interval_training)
B2 = Tkinter.Button(window, text ="Dreiklang Training", command = start_chord_3_training)
B3 = Tkinter.Button(window, text ="Vierklang Training", command = start_chord_4_training)
B4 = Tkinter.Button(window, text ="Spiele alle Akkorde", command = start_accords)


B1.pack()
B2.pack()
B3.pack()
B4.pack()
window.mainloop()
