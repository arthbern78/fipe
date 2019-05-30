import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import ttk


def btn1_click():
    print(vlr1.get())

Tela_8_comum = Tk()
Tela_8_comum.geometry('300x300+200+200')
Tela_8_comum.title("Consulta Tabela FIPE")
Tela_8_comum.resizable(False, False)

frm1 = Frame(height = 150)
frm1.pack(fill = X)
imagem = tk.PhotoImage(file = "fipe_logo.png").subsample(3, 3)
w = tk.Label(frm1, image = imagem)
w.imagem = imagem
w.pack()

frm2 = Frame()
frm2.pack(fill = X)
x1 = Label(frm2, text = 'Código FIPE:')
x1.pack()
s = "teste"
vlr1 = Entry(frm2, state = NORMAL, width = 30, textvariable = s)
vlr1.insert(0, "teste")
vlr1.pack()










frm7 = Frame(height = 100)
frm7.pack()
btn1 = Button(frm7, width = 20, text = 'OK',compound = RIGHT, command = btn1_click)
btn1.pack()

Tela_8_comum.mainloop()