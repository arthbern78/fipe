import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import ttk

def btn1_click():
    print("ola")
    Tela_10_final.destroy()
    import Tela_4_consulta
    Tela_4_consulta()

def btn2_click():
    answer = mbox.askyesnocancel("Sair", "Deseja Sair?")
    if answer == 1:
        exit()
    
Tela_1_abertura = Tk()
Tela_1_abertura.geometry('300x300+200+200')
Tela_1_abertura.title("Consulta Tabela FIPE")
Tela_1_abertura.resizable(False, False)

imagem = tk.PhotoImage(file = "fipe_logo.png")
w = tk.Label(Tela_1_abertura, image = imagem)
w.imagem = imagem
w.pack()

frm1 = Frame(height = 20)
frm1.pack()

frm2 = Frame()
frm2.pack()
btn1 = ttk.Button(frm2, text = "INICIO", width = 20, command = btn1_click)
btn1.pack()

frm3 = Frame(height = 20)
frm3.pack()

frm4 = Frame()
frm4.pack()
btn2 = ttk.Button(frm4, text = "SAIR", width = 20, command = btn2_click)
btn2.pack()

Tela_1_abertura.mainloop()