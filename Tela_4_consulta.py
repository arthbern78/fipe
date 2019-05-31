import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import ttk
import json
import requests

def btn1_click():
    f = open("veiculo.txt", "w")
    f.write("carros")
    f.close()
    Tela_4_consulta.destroy()
    import Tela_5_tipo
    
def btn2_click():
    f = open("veiculo.txt", "w")
    f.write("caminhoes")
    f.close()
    Tela_4_consulta.destroy()
    import Tela_5_tipo
def btn3_click():
    f = open("veiculo.txt", "w")
    f.write("motos")
    f.close()
    Tela_4_consulta.destroy()
    import Tela_5_tipo

Tela_4_consulta = Tk()
Tela_4_consulta.geometry('300x300+200+200')
Tela_4_consulta.title("Consulta Tabela FIPE")
Tela_4_consulta.resizable(False, False)

frm1 = Frame(height = 150)
frm1.pack(fill = X)
imagem = tk.PhotoImage(file = "fipe_logo.png").subsample(2,2)
w = tk.Label(frm1, image = imagem)
w.imagem = imagem
w.pack()

frm2 = Frame(height = 20)
frm2.pack(fill = X)

frm3 = Frame(height = 100)
frm3.pack(fill = X)
m1 = PhotoImage(file = "car.png").subsample(2,2)
btn1 = ttk.Button(frm3, text = "Carros e utilitários pequenos", width = 32, image = m1, compound = LEFT, command = btn1_click)
btn1.pack()

frm4 = Frame(height = 100)
frm4.pack(fill = X)
m2 = PhotoImage(file = "truck.png").subsample(2,2)
btn2 = ttk.Button(frm4, text = "Caminhões e Micro-ônibus", width = 32, image = m2, compound = LEFT, command = btn2_click)
btn2.pack()

frm5 = Frame(height = 100)
frm5.pack(fill = X)
m3 = PhotoImage(file = "bike.png").subsample(2,2)
btn3 = ttk.Button(frm5, text = "Motos", width = 32, image = m3, compound = LEFT, command = btn3_click)
btn3.pack()

Tela_4_consulta.mainloop()