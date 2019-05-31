import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import ttk

def btn1_click():
    Tela_1_abertura.destroy()
    import Tela_2_senha

Tela_1_abertura = Tk()
Tela_1_abertura.geometry('300x300+200+200')
Tela_1_abertura.title("Consulta Tabela FIPE")
Tela_1_abertura.resizable(False, False)

imagem = tk.PhotoImage(file = "fipe_logo.png")
w = tk.Label(Tela_1_abertura, image = imagem)
w.imagem = imagem
w.pack()

btn1 = ttk.Button(Tela_1_abertura, width = 5, command = btn1_click)
btn1.pack()
mi = PhotoImage(file = "enter.png").subsample(2,2)
btn1.config(image = mi,compound = RIGHT)

Tela_1_abertura.mainloop()