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
        #sql = "SELECT senha FROM cadastro WHERE login = '%s'"
        cur.execute("SELECT senha FROM cadastro WHERE login = '%s'" %(str(vl1.get())))
        senha = cur.fetchone()[0]
        print(senha)
        if str(senha) == str(vl2.get()):
            mbox.showinfo("Aviso", "Acesso Permitido")
            Tela_2_senha.destroy()
            import Tela_4_consulta
            Tela_4_consulta()
        else:
            mbox.showinfo("Erro", "Login e/ou Senha Incorretos")
        con.close()
    except Exception as erro:
        mbox.showinfo("Aviso", "Usuário não cadastrado")
        Tela_2_senha.destroy()
        import Tela_3_Cadastro
        Tela_3_Cadastro()
Tela_2_senha = Tk()
Tela_2_senha.geometry('300x300+200+200')
Tela_2_senha.title("senha")
Tela_2_senha.resizable(False, False)

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
lbl2 = Label(frm3, text = 'Usuário (e-mail):', font = 'Helvetica, 16')
lbl2.pack()
vl1 = Entry(frm3, width =20)
vl1.focus_set()
vl1.pack()

frm4 = Frame(height = 100)
frm4.pack(fill = X)
lbl3 = Label(frm4, text = 'Senha:', font = 'Helvetica, 16')
lbl3.pack()
vl2 = Entry(frm4, width = 20, show = "*")
vl2.pack()

frm5 = Frame(height = 20)
frm5.pack(fill = X)

frm6 = Frame(height = 20)
frm6.pack(fill = X)
btn1 = ttk.Button(frm6, width = 5, command = btn1_click)
btn1.pack()
mi = PhotoImage(file = "enter.png").subsample(2,2)
btn1.config(image = mi,compound = RIGHT)

Tela_2_senha.mainloop()