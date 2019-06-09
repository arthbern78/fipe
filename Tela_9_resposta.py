from datetime import datetime
import json
import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import ttk

f = open("veiculo.txt", "r")
veiculo = f.read()
f.close()

f = open("marca_id.txt", "r")
marca_id = f.read()
f.close()

f= open("modelo.txt", "r")
modelo_id = f.read()
f.close()

f = open("fipe.json", "r")
dados = json.load(f)
f.close()

def btn1_click():
    f = open("resultado.txt", "w")
    f.write(str(dados))
    f.close()
    mbox.showinfo("Exportação de arquivo", "Arquivo exportado!")

def btn2_click():
    Tela_9_dadososta()
    import Tela_10_final
    Tela_10_final()

# Dias da semana:
DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

MESES = [
    'janeiro', 'fevereiro', 'março', 'abril', 
    'maio', 'junho', 'julho', 'agosto', 
    'setembro', 'outubro', 'novembro', 'dezembro']

data = datetime.now()

Tela_9_dadososta = Tk()
Tela_9_dadososta.geometry('300x400+200+200')
Tela_9_dadososta.title("Consulta Tabela FIPE")
Tela_9_dadososta.resizable(False, False)

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
vlr1 = Entry(frm2, width = 36)
vlr1.insert(0, dados["fipe_codigo"])
vlr1.config(state = 'readonly')
vlr1.pack()

frm3 = Frame()
frm3.pack(fill = X)
x2 = Label(frm3, text = 'Marca:')
x2.pack()
vlr2 = Entry(frm3, width = 36)
vlr2.insert(0, dados["marca"])
vlr2.config(state = 'readonly')
vlr2.pack()

frm4 = Frame()
frm4.pack(fill = X)
x3 = Label(frm4, text = 'Modelo:')
x3.pack()
vlr3 = Entry(frm4, width = 36)
vlr3.insert(0, dados["name"])
vlr3.config(state = 'readonly')
vlr3.pack()

frm5 = Frame()
frm5.pack(fill = X)
x4 = Label(frm5, text = 'Ano / Modelo:')
x4.pack()
vlr4 = Entry(frm5, width = 36)
vlr4.insert(0, dados.get("ano_modelo") + " " + dados.get("combustivel"))
vlr4.config(state = 'readonly')
vlr4.pack()

frm6 = Frame()
frm6.pack(fill = X)
x5 = Label(frm6, text = 'Preço Médio:')
x5.pack()
vlr5 = Entry(frm6, width = 36)
vlr5.insert(0, dados.get("preco"))
vlr5.config(state = 'readonly')
vlr5.pack()

frm7 = Frame()
frm7.pack(fill = X)
x6 = Label(frm7, text = 'Data da Consulta')
x6.pack()
vlr6 = Entry(frm7, width = 36)
vlr6.insert(0, "{}, {} de {} de {} - {}:{}" .format(DIAS[data.weekday()], data.day, MESES[data.month-1], data.year, data.hour, data.minute))
vlr6.config(state = 'readonly')
vlr6.pack()

frm8 = Frame(height = 20)
frm8.pack()

frm9 = Frame(height = 100)
frm9.pack()
btn1 = Button(frm9, width = 20, text = 'Exportar',compound = RIGHT, command = btn1_click)
btn1.pack()

frm10 = Frame(height = 10)
frm10.pack()

frm11 = Frame(height = 100)
frm11.pack()
btn1 = Button(frm11, width = 20, text = 'Continuar',compound = RIGHT, command = btn2_click)
btn1.pack()

Tela_9_dadososta.mainloop()