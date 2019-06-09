import json
import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import ttk


def btn1_click():    
    for models in data.json():
        if models['name'] == var1.get():
            print(models['id'])
            #url_1 = 'http://fipeapi.appspot.com/api/1/{}/veiculo/{}/{}.json'.format(tipo_veiculo, marca_id, models['id'])
            f = open("modelo_id.txt", "w")
            f.write(models['id'])
            f.close()
            f = open("modelo.txt", "w")
            f.write(models['name'])
            f.close()
    Tela_8B_comum.destroy()
    import Tela_8C_comum
    Tela_8C_comum()

f = open("veiculo.txt", "r")
tipo_veiculo = f.read()
f.close()

f = open("marca_id.txt", "r")
marca_id = f.read()
f.close()

url = 'http://fipeapi.appspot.com/api/1/{}/veiculos/{}.json'.format(tipo_veiculo, marca_id) #recebe a URL

Tela_8B_comum = Tk()
Tela_8B_comum.geometry('300x300+200+200')
Tela_8B_comum.title("Consulta Tabela FIPE")
Tela_8B_comum.resizable(False, False)

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
data = requests.get(url = url)
list_of_models = []
for models in data.json():
    list_of_models.append(models['name'])
var1 = StringVar()
popupMenu1 = OptionMenu(frm3, var1, *list_of_models)
popupMenu1.config(width = 40)
lbl1 = Label(frm3, text="Selecione o modelo do veículo: ")
lbl1.pack()
popupMenu1.pack()

frm4 = Frame(height = 100)
frm4.pack()

frm5 = Frame(height = 100)
frm5.pack()
mi = PhotoImage(file = "enter.png").subsample(2, 2)
btn1 = Button(frm5, width = 140, image = mi,compound = RIGHT, command = btn1_click)
btn1.pack()

Tela_8B_comum.mainloop()