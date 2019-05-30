import json
import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import ttk


def btn1_click():
    print(campo1.get(), var2.get())

Tela_7_por_codigo = Tk()
Tela_7_por_codigo.geometry('300x300+200+200')
Tela_7_por_codigo.title("Consulta Tabela FIPE")
Tela_7_por_codigo.resizable(False, False)

frm1 = Frame(height = 150)
frm1.pack(fill = X)
imagem = tk.PhotoImage(file = "fipe_logo.png").subsample(2,2)
w = tk.Label(frm1, image = imagem)
w.imagem = imagem
w.pack()

frm2 = Frame(height = 20)
frm2.pack(fill = X)
lbl0 = Label(frm2, text = "Pesquisa por Código", font = "Helvetica, 14")
lbl0.pack()

frm3 = Frame(height = 100)
frm3.pack(fill = X)
campo1 = Entry(frm3, width = 30)
lbl1 = Label(frm3, text="Código FIPE:")
lbl1.pack()
campo1.focus_set()
campo1.pack()

frm4 = Frame(height = 100)
frm4.pack(fill = X)
list_of_models = ['']
var2 = StringVar()
popupMenu1 = OptionMenu(frm4, var2, *list_of_models)
popupMenu1.config(width = 20)
lbl2 = Label(frm4, text="Selecione o ano modelo:")
lbl2.pack()
popupMenu1.pack()

frm6 = Frame(height = 20)
frm6.pack()

frm5 = Frame(height = 100)
frm5.pack()
mi = PhotoImage(file = "enter.png").subsample(2, 2)
btn1 = Button(frm5, width = 140, image = mi,compound = RIGHT, command = btn1_click)
btn1.pack()

Tela_7_por_codigo.mainloop()