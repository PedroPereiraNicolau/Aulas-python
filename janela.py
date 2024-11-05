import tkinter as tk
from tkinter import messagebox

def gravar():
    messagebox.showinfo("Boa noite,","Boa noite, "+ entryNome.get()+"!")
    messagebox.showinfo("Sua idade,","Você tem : "+ entryIdade.get()+" anos!")
    messagebox.showinfo("Sua CPF,","Este é o seu CPF : "+ entryCPF.get()+"!")

janela = tk.Tk()
tela_largura = 800
tela_altura  = 600

janela.geometry(f'{tela_largura}x{tela_altura}')#antes do janela tk e depois do mainloop

labelTitulo = tk.Label(janela,text="Meu primeiro programa")#label = print
labelTitulo.place(x=350,y=10)

#Digitar o nome da pessoa
labelNome = tk.Label(janela,text="Digite seu Nome :")
labelNome.place(x=50,y=100)
entryNome = tk.Entry(janela)
entryNome.place(x=50,y=120,width=300)#entry = input

labelIdade = tk.Label(janela,text="Digite sua Idade :")
labelIdade.place(x=50,y=150)
entryIdade = tk.Entry(janela)
entryIdade.place(x=50,y=170,width=50)

labelCPF = tk.Label(janela,text="Digite seu CPF")
labelCPF.place(x=50,y=200)
entryCPF = tk.Entry(janela)
entryCPF.place(x=50,y=220,width=150)

buttonGravar = tk.Button(janela,text="Gravar",command=gravar)
buttonGravar.place(x=170,y=250,width=100)

janela.mainloop()