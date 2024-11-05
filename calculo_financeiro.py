import tkinter as tk
from tkinter import ttk,messagebox

def calcular_mensalidade():
    try:
        # Captura e valida os dados inseridos pelo usuário
        valor_financiamento = float(entryValor.get())
        taxa_juros = float(entryJuros.get()) /100# Converter taxa para decimal
        num_meses=int(entryMeses.get())

        if valor_financiamento<=0 or taxa_juros <= 0 or num_meses <=0:
            raise ValueError("Todos os valores devem ser maior que 0.")
        
               #Calcula o valor da prestação usando a fórmula da Tabela Price
        prestacao = (valor_financiamento*taxa_juros*(1 + taxa_juros)**num_meses)/((1 + taxa_juros)**num_meses - 1) #feito na aula
            # Exibe o valor da prestação
        labelResultado.config(text=f"Pestação Mensal R${prestacao:.2f}")

    except ValueError as e:
        # Exibe mensagem de erro se houver valores inválido
        messagebox.showerror("Erro", f"Entrada inválida: {e}")
janela = tk.Tk()  
janela.title = "CALCULO FINANCEIRO"
janela.geometry("300x250")

labelValor = tk.Label(janela,text="Valor Financeiro:").grid(row=0,column=0)
entryValor = tk.Entry(janela)
entryValor.grid(row=0,column=1,padx=10,pady=10)

labelJuros = tk.Label(janela,text="Juros Mensais:").grid(row=1,column=0)
entryJuros = tk.Entry(janela)
entryJuros.grid(row=1,column=1,padx=10,pady=10)

labelMeses = tk.Label(janela,text="Numero de Meses:").grid(row=2,column=0)
entryMeses = tk.Entry(janela)
entryMeses.grid(row=2,column=1,padx=10,pady=10)

btn_calcular = tk.Button(janela,text="Calcular",command=calcular_mensalidade)
btn_calcular.grid(row=3,column=0,columnspan=2,padx=10,pady=10)

labelTituloResultado = tk.Label(janela,text="Valor da mensalidade")
labelTituloResultado.grid(row=4,column=0,columnspan=2,)

labelResultado = tk.Label(janela,text="R$0.00")
labelResultado.grid(row=5,column=0,columnspan=2,)

janela.mainloop()