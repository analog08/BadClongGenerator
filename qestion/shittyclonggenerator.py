#imports the random module, as well as the Tkinter GUI module
import random

from tkinter import *
from tkinter import ttk
import tkinter.messagebox

# Creates lists for languages and gimmicks
languages = ["English", "Spanish", "French", "German", "Italian", "Latin", "Japanese", "Chinese (any version)", "Esperanto"]
gimmicks = ["with a particle system", "with a logography", "there is no word for 'to be'", "with OSV", "with a maximum lexicon of 200 words", "you have to include a wheezing noise in the phonemic inventory and use it somewhere", "made into a Creole with Portugese", "without tenses", "polysynthetic as fuck"]

# Combines random selections from the language and gimmick lists. This function gets called when the 'roll' button is pressed
def rollo():
	chosenlang = random.choice(languages)
	chosengimmick = random.choice(gimmicks)

	combo = chosenlang + ", but " + chosengimmick
	tkinter.messagebox.showinfo("the shitty cloŋ generator", combo)
	
# Creates main window
win = Tk()
frm = ttk.Frame(win, padding=50)
frm.grid()
win.title('the shitty cloŋ generator');
win.geometry("550x350+10+20")
title = ttk.Label(frm, text="the shitty cloŋ generator", font=('Helvetica 20 bold')).grid(column=1, row=0)

list = ttk.Label(text = "take a perfectly good language and add a weird feature! \n (if you get a feature that is already in the language, roll again)", font=('Calibri 15 italic'), justify=CENTER).grid(column=0, row=1)
langlist = ttk.Label(text = "\n" "languages available: English, Spanish, French, German, Italian, French, Latin, Japanese, Chinese, Esperanto", wraplength=300, justify=LEFT).grid(column=0,row=2)
gimmicklist = ttk.Label(text = "\n" "gimmicks: Particles, Logography, No verb for 'to be', OSV word order, Maximum lexicon size of 200 words, Include a wheezing noise in the phonemic inventory, Creole with Portugese, No tenses, Polysynthetic", wraplength=300, justify=LEFT).grid(column=0,row=3)

# the aformentioned 'roll' button
roll = ttk.Button(text = "roll", command=rollo).grid(column=0, row=4)

win.mainloop()


