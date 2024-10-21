import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox


class Lista:
    def __init__(self, tela):
        self.tela = tela
        titulo = "Sistema de Usuários - Pesquisa Usuários"
        self.titulo = titulo
        self.tela.title(titulo)
        self.tela.geometry("600x250")
        self.conn = sqlite3.connect("usuarios.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM usuarios")
        tot_usuarios = self.cursor.fetchall()
        self.conn.close()

        self.tree = ttk.Treeview(self.tela,
                                 columns=("ID", "Nome", "Email", "Senha"),
                                 show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Senha", text="Senha")

        for cont_usuario in tot_usuarios:
            self.tree.insert("", tk.END, values=cont_usuario)

        self.tree.pack()

        self.excluir_button = tk.Button(self.tela, text="Excluir", command=self.excluir_usuario)
        self.excluir_button.pack()

        self.alterar_button = tk.Button(self.tela, text="Alterar", command=self.alterar)
        self.alterar_button.pack()

    def excluir_usuario(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo(self.titulo, "Nenhum usuário selecionado.")
            return

        self.conn = sqlite3.connect("usuarios.db")
        self.cursor = self.conn.cursor()
        id_usuario = self.tree.item(selected_item[0], "values")[0]
        self.cursor.execute("DELETE FROM usuarios WHERE id=?", (id_usuario,))
        self.conn.commit()
        self.conn.close()
        self.tree.delete(selected_item[0])
        messagebox.showinfo(self.titulo, "Usuário excluído com sucesso.")

    def alterar(self):
        pass


if __name__ == "__main__":
    tela = tk.Tk()
    lista = Lista(tela)
    tela.mainloop()
