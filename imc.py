import tkinter as tk
from tkinter import ttk,messagebox

def calcular_imc():
    try:
        valor_peso = float(entrypeso.get())
        valor_altura = float(entryaltura.get())

        if valor_peso <= 0 or valor_altura <= 0:
            raise ValueError("Os valores devem ser maior que 0.")
        
        imc_calc = (valor_peso/(valor_altura**2))
        if imc_calc <= 18.4:
            frase = "Voce esta classifcado em magreza com\n",imc_calc,"de imc."
        elif imc_calc >= 18.5 and imc_calc <= 24.9:
            frase ="Voce esta classifcado em normal com\n",imc_calc,"de imc."
        elif imc_calc >= 25 and imc_calc <= 29.9:
            frase ="Voce esta classifcado em sobrepeso com\n",imc_calc,"de imc."
        elif imc_calc >= 30 and imc_calc <= 39.9:
            frase ="Voce esta classifcado em obesidade com\n",imc_calc,"de imc."
        elif imc_calc >= 40:
            frase ="Voce esta classifcado em obesidade grave com\n",imc_calc,"de imc."
        #messagebox.showinfo("Atenção",frase)
        imc.config(text=frase)
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")  

janela = tk.Tk()
janela.title("CALCULO IMC")
janela.geometry("300x250")


labelpeso = tk.Label(janela,text="Digite sue peso:")
labelpeso.grid(row=0,column=0)
entrypeso = tk.Entry(janela)
entrypeso.grid(row=0,column=1)

labelaltura = tk.Label(janela,text="Digite a sua altura:")
labelaltura.grid(row=1,column=0)
entryaltura = tk.Entry(janela)
entryaltura.grid(row=1,column=1)

btn_calcular = tk.Button(janela,text="Calcular",command=calcular_imc)
btn_calcular.grid(row=2,column=0,columnspan=2)

imc = tk.Label(janela,text="")
imc.grid(row=3,column=0,columnspan=2)


janela.mainloop()



