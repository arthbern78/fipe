import json
import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import ttk

def btn1_click():    
    for year in data.json():
        if year['name'] == var1.get():
            url_1 = 'http://fipeapi.appspot.com/api/1/{}/veiculo/{}/{}/{}.json'.format(tipo_veiculo, marca_id, modelo, year['id'])
            dados = requests.get(url=url_1)
            f = open("fipe.json", "w")
            json.dump(dados.json(), f, sort_keys=True, indent=4)
            f.close()
    Tela_8C_comum.destroy()
    import Tela_9_resposta
    Tela_9_resposta()

f = open("veiculo.txt", "r")
tipo_veiculo = f.read()
f.close()

f = open("marca_id.txt", "r")
marca_id = f.read()
f.close()

f = open("modelo_id.txt", "r")
modelo = f.read()
f.close() 

url = 'http://fipeapi.appspot.com/api/1/{}/veiculo/{}/{}.json'.format(tipo_veiculo, marca_id, modelo) 

Tela_8C_comum = Tk()
Tela_8C_comum.geometry('300x300+200+200')
Tela_8C_comum.title("Consulta Tabela FIPE")
Tela_8C_comum.resizable(False, False)

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
list_of_years = []
for item in data.json():
    list_of_years.append(item['name'])
var1 = StringVar()
popupMenu1 = OptionMenu(frm3, var1, *list_of_years)
popupMenu1.config(width = 40)
lbl1 = Label(frm3, text="Selecione o ano/combustível do veículo: ")
lbl1.pack()
popupMenu1.pack()

frm4 = Frame(height = 100)
frm4.pack()

frm5 = Frame(height = 100)
frm5.pack()
mi = PhotoImage(file = "enter.png").subsample(2, 2)
btn1 = Button(frm5, width = 140, image = mi,compound = RIGHT, command = btn1_click)
btn1.pack()

Tela_8C_comum.mainloop()