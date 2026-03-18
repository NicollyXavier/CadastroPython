import tkinter as tk
from tkinter import messagebox
import sqlite3

# Criar ou conectar ao banco de dados
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL           
)
""")

conn.commit()
conn.close()

# Função de cadastro
def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()

    if nome == "" or email == "" or senha == "":
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return
    
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
            (nome, email, senha)
        )
        conn.commit()
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Email já cadastrado!")
    
    conn.close()

    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_senha.delete(0, tk.END)

# Criar Janela
janela = tk.Tk()
janela.title("Cadastro de Usuário")
janela.geometry("300x250")

# Nome
tk.Label(janela, text="Nome:").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

# Email
tk.Label(janela, text="Email:").pack()
entry_email = tk.Entry(janela)
entry_email.pack()

# Senha
tk.Label(janela, text="Senha:").pack()
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack()

# Botão
tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=10)

# Rodar aplicação
janela.mainloop()