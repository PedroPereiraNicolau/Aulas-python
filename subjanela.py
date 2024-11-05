import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
def salvar_funcionario():
    ...

subjanela = tk.Tk()
subjanela.title("Adicionar funcionarios")
subjanela.geometry("400x220")#usado para predefenir o tamnaho da janela

ImagemFundo = Image.open("fundo.jpg")
ImagemResized = ImagemFundo.resize((400, 220),Image.NEAREST)
ImagemFundo = ImageTk.PhotoImage(ImagemResized)
LabelImage = tk.Label(subjanela,image=ImagemFundo)
LabelImage.image = ImagemFundo
LabelImage.place(x=0,y=0,width=400,height=220)

#campos de entrada
tk.Label(subjanela,text="Nome:").grid(row=0,column=1)
entry_Nome = tk.Entry (subjanela,width=40)#width= foi usado para aumentar a barra de pesquisa
entry_Nome.grid(row=0,column=2)

tk.Label(subjanela,text="ID:").grid(row=1,column=1)
entry_ID = tk.Entry (subjanela,width=20)
entry_ID.grid(row=1,column=2,sticky="w")

tk.Label(subjanela,text="Idade:").grid(row=2,column=1)
entry_Idade = tk.Entry (subjanela,width=10)
entry_Idade.grid(row=2,column=2,sticky="w")

tk.Label(subjanela,text="Cargo:").grid(row=3,column=1)
entry_Cargo = tk.Entry (subjanela,width=40)
entry_Cargo.grid(row=3,column=2,sticky="w")

tk.Label(subjanela,text="Departamento:").grid(row=4,column=1)
entry_Departamento = tk.Entry (subjanela,width=40)
entry_Departamento.grid(row=4,column=2,sticky="w")

tk.Label(subjanela,text="Salario:").grid(row=5,column=1)
entry_Salario = tk.Entry (subjanela,width=25)
entry_Salario.grid(row=5,column=2,sticky="w")

tk.Label(subjanela,text="Telefone:").grid(row=6,column=1)
entry_Telefone = tk.Entry (subjanela,width=20)
entry_Telefone.grid(row=6,column=2,sticky="w")

tk.Label(subjanela,text="Email:").grid(row=7,column=1)
entry_Email = tk.Entry (subjanela,width=40)
entry_Email.grid(row=7,column=2,sticky="w")#w é um dos pontos cardeais

btn_salvar = tk.Button(subjanela, text= "Salvar",width=25,command=salvar_funcionario)
btn_salvar.grid(row=8, column=2,padx=10,pady=10)

subjanela.mainloop()