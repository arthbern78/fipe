import json
#import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import ttk


def btn1_click():
    print(var1.get(), var2.get(), var3.get())

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

frm2 = Frame(height = 20)
frm2.pack(fill = X)
lbl0 = Label(frm2, text = "Pesquisa por Veículo", font = "Helvetica, 14")
lbl0.pack()

frm3 = Frame(height = 100)
frm3.pack(fill = X)
list_of_brands = ['aaa']
var1 = StringVar()
popupMenu1 = OptionMenu(frm3, var1, *list_of_brands)
popupMenu1.config(width = 20)
lbl1 = Label(frm3, text="Selecione a marca do veículo:")
lbl1.pack()
popupMenu1.pack()

frm4 = Frame(height = 100)
frm4.pack(fill = X)
list_of_models = ['bbb']
var2 = StringVar()
popupMenu2 = OptionMenu(frm4, var2, *list_of_models)
popupMenu2.config(width = 20)
lbl2 = Label(frm4, text="Selecione o modelo do veículo:")
lbl2.pack()
popupMenu2.pack()

frm5 = Frame(height = 100)
frm5.pack(fill = X)
list_of_year = ['ccc']
var3 = StringVar()
popupMenu3 = OptionMenu(frm5, var3, *list_of_year)
popupMenu3.config(width = 20)
lbl3 = Label(frm5, text="Selecione o ano do veículo:")
lbl3.pack()
popupMenu3.pack()

frm6 = Frame(height = 20)
frm6.pack()

frm7 = Frame(height = 100)
frm7.pack()
mi = PhotoImage(file = "enter.png").subsample(2, 2)
btn1 = Button(frm7, width = 140, image = mi,compound = RIGHT, command = btn1_click)
btn1.pack()

Tela_8_comum.mainloop()