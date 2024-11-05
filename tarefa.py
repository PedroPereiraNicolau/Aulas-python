import tkinter as tk  # Importa a biblioteca tkinter para interfaces gráficas
from tkinter import messagebox  # Importa o módulo para caixas de mensagem
import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import json  # Importa o módulo para trabalhar com dados em formato JSON
import os  # Importa o módulo para interagir com o sistema operacional

# Define a classe GerenciadorDeTarefas
class GerenciadorDeTarefas:
    def __init__(self, root):
        self.root = root  # Armazena a referência da janela principal
        self.root.title("Gerenciador de Tarefas")  # Define o título da janela

        # Cria um DataFrame vazio para armazenar tarefas
        self.tarefas = pd.DataFrame(columns=["Tarefa", "Concluída"])
        self.carregar_tarefas()  # Carrega tarefas ao iniciar

        # Widgets
        self.tarefa_entry = tk.Entry(root, width=40)  # Campo de entrada para a tarefa
        self.tarefa_entry.pack(pady=10)  # Adiciona o widget à janela com espaçamento

        # Botão para adicionar tarefa
        self.adicionar_button = tk.Button(root, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.adicionar_button.pack(pady=5)  # Adiciona o botão à janela

        # Botão para listar tarefas
        self.listar_button = tk.Button(root, text="Listar Tarefas", command=self.listar_tarefas)
        self.listar_button.pack(pady=5)  # Adiciona o botão à janela

        # Botão para marcar tarefa como concluída
        self.marcar_button = tk.Button(root, text="Marcar como Concluída", command=self.marcar_concluida)
        self.marcar_button.pack(pady=5)  # Adiciona o botão à janela

        # Botão para excluir tarefa
        self.excluir_button = tk.Button(root, text="Excluir Tarefa", command=self.excluir_tarefa)
        self.excluir_button.pack(pady=5)  # Adiciona o botão à janela

        # Listbox para mostrar as tarefas
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)  # Adiciona a Listbox à janela

    # Método para adicionar nova tarefa
    def adicionar_tarefa(self):
        tarefa_nome = self.tarefa_entry.get()  # Obtém o texto da entrada
        if tarefa_nome:  # Verifica se o campo não está vazio
            # Cria um novo DataFrame para a nova tarefa
            nova_tarefa = pd.DataFrame({"Tarefa": [tarefa_nome], "Concluída": [False]})
            # Concatena a nova tarefa ao DataFrame existente
            self.tarefas = pd.concat([self.tarefas, nova_tarefa], ignore_index=True)
            self.tarefa_entry.delete(0, tk.END)  # Limpa o campo de entrada
            self.listar_tarefas()  # Atualiza a lista após adicionar
        else:
            messagebox.showwarning("Advertência", "Digite o nome da tarefa.")  # Aviso se o campo estiver vazio

    # Método para listar todas as tarefas
    def listar_tarefas(self):
        self.listbox.delete(0, tk.END)  # Limpa a Listbox
        if self.tarefas.empty:  # Verifica se não há tarefas
            self.listbox.insert(tk.END, "Nenhuma tarefa cadastrada.")  # Mensagem se não houver tarefas
        else:
            # Itera sobre as tarefas e as insere na Listbox
            for index, row in self.tarefas.iterrows():
                status = "Concluída" if row["Concluída"] else "Não Concluída"  # Define o status da tarefa
                self.listbox.insert(tk.END, f"{index + 1}. {row['Tarefa']} - {status}")  # Insere na lista

        self.salvar_tarefas()  # Salva as tarefas sempre que listar

    # Método para marcar uma tarefa como concluída
    def marcar_concluida(self):
        try:
            numero = int(self.listbox.curselection()[0])  # Obtém o índice da tarefa selecionada
            self.tarefas.at[numero, "Concluída"] = True  # Marca a tarefa como concluída
            self.listar_tarefas()  # Atualiza a lista após marcar
        except IndexError:
            messagebox.showwarning("Advertência", "Selecione uma tarefa para marcar como concluída.")  # Aviso se não houver seleção

    # Método para excluir uma tarefa
    def excluir_tarefa(self):
        try:
            numero = int(self.listbox.curselection()[0])  # Obtém o índice da tarefa selecionada
            self.tarefas = self.tarefas.drop(numero).reset_index(drop=True)  # Remove a tarefa do DataFrame
            self.listar_tarefas()  # Atualiza a lista após excluir
        except IndexError:
            messagebox.showwarning("Advertência", "Selecione uma tarefa para excluir.")  # Aviso se não houver seleção

    # Método para salvar tarefas em um arquivo JSON
    def salvar_tarefas(self):
        with open('tarefas.json', 'w') as f:  # Abre o arquivo tarefas.json para escrita
            json.dump(self.tarefas.to_dict(orient='records'), f)  # Converte o DataFrame e escreve no arquivo
            messagebox.showinfo("Sucesso", "Tarefas salvas com sucesso!")  # Mensagem de sucesso

    # Método para carregar tarefas de um arquivo JSON
    def carregar_tarefas(self):
        if os.path.exists('tarefas.json'):  # Verifica se o arquivo existe
            with open('tarefas.json', 'r') as f:  # Abre o arquivo tarefas.json para leitura
                tarefas_carregadas = json.load(f)  # Lê as tarefas do arquivo
                self.tarefas = pd.DataFrame(tarefas_carregadas)  # Converte para um DataFrame

# Execução do programa
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    gerenciador = GerenciadorDeTarefas(root)  # Instancia a classe GerenciadorDeTarefas
    root.mainloop()  # Inicia o loop principal da interface
