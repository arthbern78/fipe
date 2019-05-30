from datetime import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import ttk


def btn1_click():
    print(tkvar1.get(), tkvar2.get())

Tela_6_periodo = Tk()
Tela_6_periodo.geometry('300x300+200+200')
Tela_6_periodo.title("Consulta Tabela FIPE")
Tela_6_periodo.resizable(False, False)

frm1 = Frame(height = 150)
frm1.pack(fill = X)
imagem = tk.PhotoImage(file = "fipe_logo.png").subsample(2,2)
w = tk.Label(frm1, image = imagem)
w.imagem = imagem
w.pack()

frm2 = Frame(height = 20)
frm2.pack(fill = X)
lbl0 = Label(frm2, text = "Mês/Ano de Referência", font = "Helvetica, 16")
lbl0.pack()

frm3 = Frame(height = 100)
frm3.pack(fill = X)
list_of_months = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
tkvar1 = IntVar(value = datetime.now().month)
popupMenu = OptionMenu(frm3, tkvar1, *list_of_months)
popupMenu.config(width = 20)
lbl1 = Label(frm3, text="Mês:")
lbl1.pack()
popupMenu.pack()

frm4 = Frame(height = 100)
frm4.pack(fill = X)
list_of_years = []
the_year = datetime.now().year
start_year = datetime.now().year - 20
while the_year >= start_year:
    list_of_years.append(the_year)
    the_year -= 1
tkvar2 = IntVar(value = datetime.now().year)
popupMenu1 = OptionMenu(frm4, tkvar2, *list_of_years)
popupMenu1.config(width = 20)
lbl2 = Label(frm4, text="Ano:")
lbl2.pack()
popupMenu1.pack()

frm6 = Frame(height = 20)
frm6.pack()

frm5 = Frame(height = 100)
frm5.pack()
mi = PhotoImage(file = "enter.png").subsample(2, 2)
btn1 = Button(frm5, width = 140, image = mi,compound = RIGHT, command = btn1_click)
btn1.pack()

Tela_6_periodo.mainloop()