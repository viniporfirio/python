import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3

class Profissao:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de restaurante - Cadastro de Profissões")
        self.root.geometry("300x200")


        self.conn = sqlite3.connect("restaurante.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS profissoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                ativo INT
            )
        """)


        self.nome_label = tk.Label(root, text="Nome:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(root, width=30)
        self.nome_entry.pack()


        self.frame_cima = Frame(self.root)
        self.frame_cima.pack()


        self.radio_valor = IntVar()
        self.radio_valor.set(1)

        self.label = Label(self.frame_cima, text='A situação é: ')
        self.label.pack(anchor='w')

        self.ativo = Radiobutton(self.frame_cima, text='Ativa',
                                 variable=self.radio_valor, value=1)
        self.ativo.pack(anchor='w')

        self.inativo = Radiobutton(self.frame_cima, text='Inativa',
                                   variable=self.radio_valor, value=2)
        self.inativo.pack(anchor='w')


        self.cadastro_button = tk.Button(root,
                                         text="Cadastrar",
                                         command=self.cadastro)
        self.cadastro_button.pack()

    def cadastro(self):
        nome = self.nome_entry.get()
        ativo = self.radio_valor.get()
        
        if nome:  
            self.cursor.execute(
                "INSERT INTO profissoes (nome, ativo) VALUES ()",
                (nome, ativo)
            )
            self.conn.commit()
            messagebox.showinfo("Sistema de cadastro de profissões", "O cadastro foi realizado com sucesso!")
            self.nome_entry.delete(0, END)  
        else:
            messagebox.showwarning("Erro de cadastro", "O nome da profissão deve ser preenchido.")

if __name__ == "__main__":
    root = tk.Tk()
    profissao = Profissao(root)
    root.mainloop()
