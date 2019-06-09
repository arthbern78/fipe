import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import ttk
import json
import requests

f = open("veiculo.txt", 'r')
veiculo = f.read()

def btn1_click():
    Tela_5_tipo.destroy()
    import Tela_8A_comum
    Tela_8A_comum()

def btn2_click():
    Tela_5_tipo.destroy()
    import Tela_7_por_codigo
    Tela_7_por_codigo()

Tela_5_tipo = Tk()
Tela_5_tipo.geometry('300x300+200+200')
Tela_5_tipo.title("Consulta Tabela FIPE")
Tela_5_tipo.resizable(False, False)

frm1 = Frame(height = 150)
frm1.pack(fill = X)
imagem = tk.PhotoImage(file = "fipe_logo.png").subsample(2,2)
w = tk.Label(frm1, image = imagem)
w.imagem = imagem
w.pack()

frm4 = Frame(height = 20)
frm4.pack(fill = X)

frm1 = Frame(height = 150)
frm1.pack(fill = X)
btn1 = Button(frm1, height = 3, width = 30, text = "PESQUISA COMUM", font = ("Helvetica", 12), command = btn1_click)
btn1.pack()

frm2 = Frame(height = 20)
frm2.pack(fill = X)

frm3 = Frame(height = 150)
frm3.pack(fill = X)
btn2 = Button(frm3, height = 3, width = 30, text = "PESQUISA CÓDIGO FIPE", font = ("Helvetica", 12), command = btn2_click)
btn2.pack()


Tela_5_tipo.mainloop()