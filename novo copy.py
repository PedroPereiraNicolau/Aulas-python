import tkinter as tk
from tkinter import ttk,messagebox
import sqlite3

#conexao com banco de dados SQLite
conexao = sqlite3.connect("funcionarios.db")
cursor = conexao.cursor()


#cria a tabela se ela nao existir
cursor.execute("""CREATE TABLE IF NOT EXISTS funcionarios ( 
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               idade INTEGER,
               cargo TEXT,
               departamento TEXT,
               salario REAL,
               telefone TEXT,
               email TEXT)""")
conexao.commit()#realiza a gravação dos dados
# Função para buscar funcionários no banco de dados
def buscar_funcionarios(nome=""):
    cursor.execute("SELECT * FROM funcionarios WHERE nome LIKE ?", ('%' + nome + '%',))
    return cursor.fetchall()#retorna os nomes

def atualizar_lista(nome=""):
    for row in tree.get_children():
        tree.delete(row)
    funcionarios = buscar_funcionarios(nome)
    for funcionario in funcionarios:
        tree.insert("", "end", values=funcionario)

def adicionar_funcionario():
    def salvar_funcionario():
        nome = entry_nome.get()
        idade = entry_idade.get()
        cargo = entry_cargo.get()
        departamento = entry_departamento.get()
        salario = entry_salario.get()
        telefone = entry_telefone.get()
        email = entry_email.get()

        if nome and idade and cargo and departamento and salario and telefone and email:
            cursor.execute("INSERT INTO funcionarios (nome, idade, cargo, departamento, salario, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                           (nome, idade, cargo, departamento, salario, telefone, email))
            conexao.commit()
            atualizar_lista()
            janela_add.destroy()
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    # Janela para adicionar funcionário
    janela_add = tk.Toplevel(janelaprincipal)#toplevel e uma subjanela
    janela_add.title("Adicionar Funcionário")
    janela_add.geometry("400x220")
    
    # Campos de entrada
    tk.Label(janela_add, text="Nome").grid(row=0, column=0)
    entry_nome = tk.Entry(janela_add)
    entry_nome.grid(row=0, column=1)

    tk.Label(janela_add, text="Idade").grid(row=1, column=0)
    entry_idade = tk.Entry(janela_add)
    entry_idade.grid(row=1, column=1)

    tk.Label(janela_add, text="Cargo").grid(row=2, column=0)
    entry_cargo = tk.Entry(janela_add)
    entry_cargo.grid(row=2, column=1)

    tk.Label(janela_add, text="Departamento").grid(row=3, column=0)
    entry_departamento = tk.Entry(janela_add)
    entry_departamento.grid(row=3, column=1)

    tk.Label(janela_add, text="Salário").grid(row=4, column=0)
    entry_salario = tk.Entry(janela_add)
    entry_salario.grid(row=4, column=1)

    tk.Label(janela_add, text="Telefone").grid(row=5, column=0)
    entry_telefone = tk.Entry(janela_add)
    entry_telefone.grid(row=5, column=1)

    tk.Label(janela_add, text="Email").grid(row=6, column=0)
    entry_email = tk.Entry(janela_add)
    entry_email.grid(row=6, column=1)

    # Botão para salvar o funcionário
    btn_salvar = tk.Button(janela_add, text="Salvar", command=salvar_funcionario)
    btn_salvar.grid(row=7, columnspan=2)
def alterar_funcionario():
    ...
def deletar_funcionario():
    ...
def salvar_funcionario():
    ...

janelaprincipal = tk.Tk()
janelaprincipal.title("DPExpress")#titulo 

tk.Label(janelaprincipal, text ="Pesquisar por Nome: ").grid(row=0, column=0, padx=10, pady=10)
entry_pesquisa = tk.Entry(janelaprincipal)
entry_pesquisa.grid(row=0, column=1, padx=10, pady=10)
entry_pesquisa.bind("<KeyRealease>"),lambda event: atualizar_lista(entry_pesquisa.get())

btn_adicionar = tk.Button(janelaprincipal, text= "Adicionar", command=adicionar_funcionario)
btn_adicionar.grid(row=0, column=2, padx=10, pady=10)

btn_alterar = tk.Button(janelaprincipal, text= "Alterar", command=alterar_funcionario)
btn_alterar.grid(row=0, column=3, padx=10, pady=10)

btn_deletar = tk.Button(janelaprincipal, text= "Deletar", command=deletar_funcionario)
btn_deletar.grid(row=0, column=4, padx=10, pady=10)

tree = ttk.Treeview(janelaprincipal, columns=("ID","Nome","Idade","Cargo","Departamento","Salario","Telefone","Email"),show="headings")
tree.heading("ID",              text="ID")
tree.heading("Nome",            text="Nome")
tree.heading("Idade",           text="Idade")
tree.heading("Cargo",           text="Cargo")
tree.heading("Departamento",    text="Departamento")
tree.heading("Salario",         text="Salário")
tree.heading("Telefone",        text="Telefone")
tree.heading("Email",           text="Email")
tree.grid(row=1,column=0,columnspan=5,padx=10,pady=10)


janelaprincipal.mainloop()