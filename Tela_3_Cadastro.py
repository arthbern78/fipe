import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import ttk


def btn1_click():
    import psycopg2 as pg
    try:
        con = pg.connect(
            database="fipe",
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port="5432"
        )
        cur = con.cursor()
        sql = "INSERT INTO cadastro (login, senha, email, sexo) values (%s,%s,%s,%s)"
        cur.execute(cur.mogrify(sql, (str(vl1.get()), str(vl3.get()), str(vl2.get()), str(var.get()))))
        mbox.showinfo("Aviso", "Cadastro Realizado com Sucesso")
        con.commit()
        con.close()
        Tela_3_Cadastro.destroy()
        import Tela_2_senha
        Tela_2_senha()
    except Exception as erro:
        print(erro)

Tela_3_Cadastro = Tk()
Tela_3_Cadastro.geometry('300x300+200+200')
Tela_3_Cadastro.title("Consulta Tabela FIPE")
Tela_3_Cadastro.resizable(False, False)


lbl0 = Label(text = 'CADASTRO', justify=LEFT, font=("Helvetica", 18))
lbl0.pack()

frm1 = Frame(height = 60)
frm1.pack(fill = X)
lbl1 = Label(frm1, height = 2, text = 'Login', justify=LEFT, font = 'Helvetica, 12')
lbl1.pack()
vl1 = Entry(frm1, width = 45)
vl1.focus_set()
vl1.pack()

frm6 = Frame(height = 60)
frm6.pack()
var = StringVar(value = 'masculino')
masculino = ttk.Radiobutton(frm6, text='masculino', variable=var)
masculino.config(width=12, value='masculino')
masculino.grid(row=0, column=0)
feminino = ttk.Radiobutton(frm6, text='feminino', variable=var)
feminino.config(width=12, value='feminino')
feminino.grid(row=0, column=1)
no_binary = ttk.Radiobutton(frm6, text='não binário', variable=var)
no_binary.config(width=12, value='não binário')
no_binary.grid(row=0, column=2)

frm2 = Frame(height = 60)
frm2.pack(fill = X)
lbl2 = Label(frm2, height = 2, text = 'e-mail', justify=LEFT, font = 'Helvetica, 12')
lbl2.pack()
vl2 = Entry(frm2, width = 45)
vl2.pack()

frm3 = Frame(height = 60)
frm3.pack(fill = X)
lbl3 = Label(frm3, height = 2, text = 'senha', justify=LEFT, font = 'Helvetica, 12')
lbl3.pack()
vl3 = Entry(frm3, width = 45)
vl3.pack()

frm4 = Frame(height = 20)
frm4.pack(fill = X)

frm5 = Frame(height = 20)
frm5.pack(fill = X)
mi = PhotoImage(file = "acessar.png").subsample(1,1)
btn1 = ttk.Button(frm5, width = 5, image = mi,compound = RIGHT, command = btn1_click)
btn1.pack()

Tela_3_Cadastro.mainloop()