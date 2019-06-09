import json
import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import ttk


def btn1_click():    
    for marca in data.json():
        if marca['name'] == var1.get():
            marca_id = marca['id']
            print(marca_id)
            f = open("marca_id.txt", "w")
            f.write(str(marca_id))
            f.close()
    Tela_8A_comum.destroy()
    import Tela_8B_comum
    Tela_8B_comum()
    
f = open("veiculo.txt", "r")
tipo_veiculo = f.read()
f.close()

Tela_8A_comum = Tk()
Tela_8A_comum.geometry('300x300+200+200')
Tela_8A_comum.title("Consulta Tabela FIPE")
Tela_8A_comum.resizable(False, False)

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
url = 'http://fipeapi.appspot.com/api/1/{}/marcas.json'.format(tipo_veiculo)
data = requests.get(url = url)
list_of_brands = []
for marca in data.json():
    list_of_brands.append(marca['name'])
var1 = StringVar()
popupMenu1 = OptionMenu(frm3, var1, *list_of_brands)
popupMenu1.config(width = 20)
lbl1 = Label(frm3, text="Selecione a marca do veículo:")
lbl1.pack()
popupMenu1.pack()

frm4 = Frame(height = 100)
frm4.pack()

frm5 = Frame(height = 100)
frm5.pack()
mi = PhotoImage(file = "enter.png").subsample(2, 2)
btn1 = Button(frm5, width = 140, image = mi,compound = RIGHT, command = btn1_click)
btn1.pack()

Tela_8A_comum.mainloop()