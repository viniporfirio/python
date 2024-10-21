import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class Listaprof:
       def __init__(self,  tela):
              self.tela = tela
              titulo = "Sistema de restaurante - Pesquisa Profissões"
              self.titulo = titulo
              self.tela.geometry("600x300")
              self.conn = sqlite3.connect("restaurante.db")
              self.cursor = self.conn.cursor()
              self.cursor.execute("SELECT * FROM profissoes")
              tot_profissoes = self.cursor.fetchall()
              self.conn.close()
              self.tree = ttk.Treeview(self.tela,
                                          columns=("ID",  "Nome",  "Ativo"),
                                          show="headings")
              self.tree.heading("ID", text="ID")
              self.tree.heading("Nome", text="Nome")
              self.tree.heading("Ativo", text="Ativo")

              for cont_profissao in tot_profissoes:
                     self.tree.insert(  "", tk.END, values=cont_profissao)

              self.tree.pack()
if __name__  ==  "__main__":
       tela = tk.Tk()
       listin = Listaprof(tela)
       tela.mainloop()
