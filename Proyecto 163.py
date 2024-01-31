# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:02:31 2024

@author: anyta
"""

from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.geometry("400x400")
root.title("Eres mi herman@ perdid@?")

respuesta_rb = StringVar(value = "0")

question1 = Label(root, text = "Te gusta Sonic?")
question1.pack()
radiob_1 = Radiobutton(root, text = "Sí!!!", variable = respuesta_rb, value = "si")
radiob_1.pack()
radiob_2 = Radiobutton(root, text = "No realmente", variable = respuesta_rb, value = "si")
radiob_2.pack()

respuesta_rb2 = StringVar(value = "0")

question2 = Label(root, text = "Te gusta Kirby?")
question2.pack()
radiob_3 = Radiobutton(root, text = "Sí!!!", variable = respuesta_rb2, value = "si")
radiob_3.pack()
radiob_4 = Radiobutton(root, text = "No realmente", variable = respuesta_rb2, value = "si")
radiob_4.pack()

respuesta_rb3 = StringVar(value = "0")

question3 = Label(root, text = "Te gusta Mario?")
question3.pack()
radiob_5 = Radiobutton(root, text = "Sí!!!", variable = respuesta_rb3, value = "si")
radiob_5.pack()
radiob_6 = Radiobutton(root, text = "No realmente", variable = respuesta_rb3, value = "si")
radiob_6.pack()

respuesta_rb4 = StringVar(value = "0")

question4 = Label(root, text = "Te gustan las espadas legendarias?")
question4.pack()
radiob_7 = Radiobutton(root, text = "Sí!!!", variable = respuesta_rb4, value = "si")
radiob_7.pack()
radiob_8 = Radiobutton(root, text = "No realmente", variable = respuesta_rb4, value = "si")
radiob_8.pack()

def Revisemos_si_eres_familiar():
    score = 0
    if respuesta_rb.get() == "si":
        score = score + 20
        print(score)
    if respuesta_rb2.get() == "si":
        score = score + 20
        print(score)
    if respuesta_rb3.get() == "si":
        score = score + 20
        print(score)
    if respuesta_rb4.get() == "si":
        score = score + 20
        print(score)
        
        if score <= 20:
            showinfo("Calculando", "Aléjate desconocid@!!!!!")
        elif score > 20 and score <= 40:
            showinfo("Calculando", "Tal vez un/una prim@ lejan@")
        elif score > 40 and score <= 60:
            showinfo("Calculando", "Eres un/una prim@ cercan@ probablemente")
        else:
            showinfo("Calculando", "Por fin te encuentro herman@!!!!")
            
btn = Button(root, text = "Veamos si eres familia", command = Revisemos_si_eres_familiar)
btn.pack()

root.mainloop()