import tkinter as tk
from tkinter import messagebox
import sqlite3


class loginSystem:
    def __init__(self, root):
         self.root = root
         self.root.title("Sistema de Login")
         self.root.geometry("600x300")
         self.conn = sqlite3.connect('usuarios.db')
         self.cursor = self.conn.cursor()
         self.cursor.execute("""
              CREATE TABLE IF NOT EXISTS usuarios (
                  id INTEGER PRIMARY KEY,
                  nome TEXT,
                  email TEXT, 
                  senha TEXT
              )
         """)

         self.nome_label = tk.Label(root, text="Nome:")
         self.nome_label.pack()
         self.nome_entry = tk.Entry(root, width=30)
         self.nome_entry.pack()

         self.email_label = tk.Label(root, text="Email:")
         self.email_label.pack()
         self.email_entry = tk.Entry(root, width=30) 
         self.email_entry.pack()

         self.senha_label = tk.Label(root, text="Senha:")
         self.senha_label.pack()
         self.senha_entry = tk.Entry(root, width=30, show="*")
         self.senha_entry.pack()

         self.login_button = tk.Button(root, text="Login", command=self.login)
         self.login_button.pack()

         self.cadastro_button = tk.Button(root, text="Cadastrar", command=self.cadastro)
         self.cadastro_button.pack()

    def login(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        self.cursor.execute("SELECT * FROM usuarios WHERE email=? AND senha=?", (email, senha))
        usuario = self.cursor.fetchone()

        if usuario:
            messagebox.showinfo("Login", "Bem-vindo, " + nome)
            self.root.destroy()

        else:
            messagebox.showerror("Login", "Email ou senha incorretos.")

    def cadastro(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        self.cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?,?,?)", (nome, email, senha))
        self.conn.commit()
        messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")


if __name__ == "__main__":
     root = tk.Tk()
     login_system = loginSystem(root)
     root.mainloop()


