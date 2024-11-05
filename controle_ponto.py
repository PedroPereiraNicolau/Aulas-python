import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sqlite3

class PontoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Controle de Ponto Simples")
        self.root.geometry("600x600")

        # Conectar ao banco de dados
        self.conn = sqlite3.connect('controle_ponto.db')
        self.create_table()

        # Lista para armazenar os registros
        self.funcionarios = self.load_funcionarios()

        # Layout da interface
        self.create_widgets()

    def create_table(self):
        # Cria a tabela se não existir
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS funcionarios (
                    id TEXT PRIMARY KEY,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    entrada TEXT,
                    saida TEXT,
                    tempo_trabalhado TEXT
                )
            ''')

    def load_funcionarios(self):
        # Carrega funcionários do banco de dados
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM funcionarios")
        funcionarios = []
        for row in cursor.fetchall():
            funcionarios.append({
                "id": row[0],
                "nome": row[1],
                "idade": row[2],
                "entrada": row[3],
                "saida": row[4],
                "tempo_trabalhado": row[5]
            })
        return funcionarios

    def create_widgets(self):
        # Frame para registro de funcionário
        frame_registro = tk.Frame(self.root)
        frame_registro.pack(pady=10)

        # Labels e entradas alinhadas
        tk.Label(frame_registro, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(frame_registro)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_registro, text="Nome:").grid(row=0, column=2, padx=5, pady=5)
        self.nome_entry = tk.Entry(frame_registro)
        self.nome_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_registro, text="Idade:").grid(row=0, column=4, padx=5, pady=5)
        self.idade_entry = tk.Entry(frame_registro)
        self.idade_entry.grid(row=0, column=5, padx=5, pady=5)

        # Botão para registrar funcionário
        self.btn_registrar = tk.Button(self.root, text="Registrar Funcionário", command=self.registrar_funcionario)
        self.btn_registrar.pack(pady=10)

        # Treeview para exibir funcionários
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nome", "Idade", "Entrada", "Saída", "Tempo Trabalhado"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Idade", text="Idade")
        self.tree.heading("Entrada", text="Entrada")
        self.tree.heading("Saída", text="Saída")
        self.tree.heading("Tempo Trabalhado", text="Tempo Trabalhado")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Frame para botões de ponto
        frame_botoes = tk.Frame(self.root)
        frame_botoes.pack(pady=10)

        self.btn_entrada = tk.Button(frame_botoes, text="Marcar Entrada", command=self.marcar_entrada)
        self.btn_entrada.grid(row=0, column=0, padx=10)

        self.btn_saida = tk.Button(frame_botoes, text="Marcar Saída", command=self.marcar_saida)
        self.btn_saida.grid(row=0, column=1, padx=10)

        # Label para exibir mensagens
        self.mensagem = tk.Label(self.root, text="")
        self.mensagem.pack(pady=10)

        self.atualizar_treeview()  # Atualiza a árvore na inicialização

    def registrar_funcionario(self):
        # Registra o funcionário no banco de dados
        id_funcionario = self.id_entry.get()
        nome_funcionario = self.nome_entry.get()
        idade_funcionario = self.idade_entry.get()

        if id_funcionario and nome_funcionario and idade_funcionario:
            with self.conn:
                self.conn.execute("INSERT INTO funcionarios (id, nome, idade) VALUES (?, ?, ?)",
                                  (id_funcionario, nome_funcionario, idade_funcionario))
            self.funcionarios.append({
                "id": id_funcionario,
                "nome": nome_funcionario,
                "idade": idade_funcionario,
                "entrada": None,
                "saida": None,
                "tempo_trabalhado": None
            })
            self.atualizar_treeview()
            self.mensagem.config(text=f"Funcionário {nome_funcionario} registrado com sucesso!")
            self.clear_entries()
        else:
            self.mensagem.config(text="Por favor, preencha todos os campos.")

    def clear_entries(self):
        # Limpa os campos de entrada
        self.id_entry.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)
        self.idade_entry.delete(0, tk.END)

    def atualizar_treeview(self):
        # Atualiza o Treeview com os funcionários registrados
        for row in self.tree.get_children():
            self.tree.delete(row)
        for funcionario in self.funcionarios:
            self.tree.insert("", "end", values=(
                funcionario["id"],
                funcionario["nome"],
                funcionario["idade"],
                funcionario['entrada'] if funcionario['entrada'] else "",
                funcionario['saida'] if funcionario['saida'] else "",
                funcionario['tempo_trabalhado'] if funcionario['tempo_trabalhado'] else ""
            ))

    def marcar_entrada(self):
        selection = self.tree.selection()
        if not selection:
            self.mensagem.config(text="Selecione um funcionário.")
            return

        index = self.tree.index(selection[0])
        if self.funcionarios[index]['entrada'] is not None:
            self.mensagem.config(text="Entrada já registrada.")
            return

        agora = datetime.now()
        self.funcionarios[index]['entrada'] = agora  # Armazena a data e hora de entrada

        # Atualiza o banco de dados
        with self.conn:
            self.conn.execute("UPDATE funcionarios SET entrada = ? WHERE id = ?",
                              (agora.strftime('%Y-%m-%d %H:%M:%S'), self.funcionarios[index]['id']))

        self.atualizar_treeview()  # Atualiza o Treeview para mostrar a hora de entrada
        self.mensagem.config(text=f"Entrada registrada para {self.funcionarios[index]['nome']}: {agora.strftime('%H:%M:%S')}")

    def marcar_saida(self):
        selection = self.tree.selection()
        if not selection:
            self.mensagem.config(text="Selecione um funcionário.")
            return

        index = self.tree.index(selection[0])
        if self.funcionarios[index]['entrada'] is None:
            self.mensagem.config(text="Entrada não registrada.")
            return

        agora = datetime.now()
        self.funcionarios[index]['saida'] = agora  # Armazena a data e hora de saída

        # Calcula horas trabalhadas
        entrada = datetime.strptime(self.funcionarios[index]['entrada'].strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        tempo_trabalhado = agora - entrada  # Calcula a diferença entre saída e entrada
        total_horas = tempo_trabalhado.total_seconds()

        # Formatação do tempo trabalhado em horas, minutos e segundos
        horas = int(total_horas // 3600)
        minutos = int((total_horas % 3600) // 60)
        segundos = int(total_horas % 60)

        # Registra as informações no banco de dados
        with self.conn:
            self.conn.execute("UPDATE funcionarios SET saida = ?, tempo_trabalhado = ? WHERE id = ?",
                              (agora.strftime('%Y-%m-%d %H:%M:%S'), f"{horas}h {minutos}m {segundos}s", self.funcionarios[index]['id']))

        self.mensagem.config(text=f"Saída registrada para {self.funcionarios[index]['nome']}: {agora.strftime('%H:%M:%S')}")
        self.atualizar_treeview()  # Atualiza o Treeview para mostrar a saída e o tempo trabalhado

if __name__ == "__main__":
    root = tk.Tk()
    app = PontoApp(root)
    root.mainloop()
