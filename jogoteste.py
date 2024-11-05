import tkinter as tk
from tkinter import messagebox

class ClickerGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo Clicker")

        self.score = 0
        self.click_multiplier = 1000  # Começa em 1000
        self.item_cost = 10
        self.auto_clickers = 0
        self.auto_clicker_cost = 50
        self.clicks_this_second = 0
        self.cps_multiplier = 1
        self.cps_upgrade_cost = 100  # Custo para o upgrade de CPS
        self.fast_mode = False  # Variável para controlar o modo rápido

        self.score_label = tk.Label(master, text="Pontos: 0", font=("Helvetica", 16))
        self.score_label.pack()

        self.cps_label = tk.Label(master, text="Cliques por Segundo: 0", font=("Helvetica", 12))
        self.cps_label.pack(pady=5)

        self.click_button = tk.Button(master, text="Clique Aqui!", command=self.increment_score, font=("Helvetica", 16))
        self.click_button.pack(pady=20)

        self.shop_label = tk.Label(master, text="Loja", font=("Helvetica", 16))
        self.shop_label.pack(pady=10)

        self.shop_info_label = tk.Label(master, text=f"Custo do Item: {self.item_cost} Pontos\nMultiplicador: {self.click_multiplier}x", font=("Helvetica", 14))
        self.shop_info_label.pack()

        self.buy_button = tk.Button(master, text="Comprar Item de Clique", command=self.buy_item, font=("Helvetica", 14))
        self.buy_button.pack(pady=5)

        self.auto_clicker_info_label = tk.Label(master, text=f"Custo do Auto Clique: {self.auto_clicker_cost} Pontos\nAuto Clicadores: {self.auto_clickers}", font=("Helvetica", 14))
        self.auto_clicker_info_label.pack(pady=10)

        self.buy_auto_clicker_button = tk.Button(master, text="Comprar Auto Clique", command=self.buy_auto_clicker, font=("Helvetica", 14))
        self.buy_auto_clicker_button.pack(pady=5)

        self.cps_upgrade_info_label = tk.Label(master, text=f"Custo do Upgrade de CPS: {self.cps_upgrade_cost} Pontos", font=("Helvetica", 14))
        self.cps_upgrade_info_label.pack(pady=10)

        self.buy_cps_upgrade_button = tk.Button(master, text="Comprar Upgrade de CPS", command=self.buy_cps_upgrade, font=("Helvetica", 14))
        self.buy_cps_upgrade_button.pack(pady=5)

        self.fast_mode_button = tk.Button(master, text="Ativar Auto Clique Rápido", command=self.toggle_fast_mode, font=("Helvetica", 14))
        self.fast_mode_button.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reiniciar", command=self.reset_score, font=("Helvetica", 16))
        self.reset_button.pack(pady=20)

        self.master.after(1000, self.update_cps)  # Chama a função de atualização do CPS a cada segundo
        self.fast_mode_timer = None  # Timer para modo rápido

    def increment_score(self):
        self.score += self.click_multiplier
        self.clicks_this_second += 1
        self.score_label.config(text=f"Pontos: {self.score}")

    def buy_item(self):
        if self.score >= self.item_cost:
            self.score -= self.item_cost
            self.click_multiplier += 1
            self.item_cost = int(self.item_cost * 1.5)  # Aumenta o custo do próximo item
            self.update_shop_info()
        else:
            messagebox.showinfo("Compra inválida", "Você não tem pontos suficientes!")

    def buy_auto_clicker(self):
        if self.score >= self.auto_clicker_cost:
            self.score -= self.auto_clicker_cost
            self.auto_clickers += 1
            self.auto_clicker_cost = int(self.auto_clicker_cost * 1.5)  # Aumenta o custo do próximo auto clicador
            self.update_auto_clicker_info()
        else:
            messagebox.showinfo("Compra inválida", "Você não tem pontos suficientes!")

    def buy_cps_upgrade(self):
        if self.score >= self.cps_upgrade_cost:
            self.score -= self.cps_upgrade_cost
            self.click_multiplier += 1000  # Aumenta em 1000 a cada upgrade
            self.cps_upgrade_cost = int(self.cps_upgrade_cost * 1.5)  # Aumenta o custo do próximo upgrade
            self.update_cps_upgrade_info()
        else:
            messagebox.showinfo("Compra inválida", "Você não tem pontos suficientes!")

    def toggle_fast_mode(self):
        self.fast_mode = not self.fast_mode  # Alterna o modo rápido
        if self.fast_mode:
            self.fast_mode_button.config(text="Desativar Auto Clique Rápido")
            self.start_fast_mode()
        else:
            self.fast_mode_button.config(text="Ativar Auto Clique Rápido")
            self.stop_fast_mode()

    def start_fast_mode(self):
        self.fast_mode_timer = self.master.after(10, self.fast_click)

    def stop_fast_mode(self):
        if self.fast_mode_timer:
            self.master.after_cancel(self.fast_mode_timer)
            self.fast_mode_timer = None

    def fast_click(self):
        # Ganha pontos de acordo com o multiplicador do clique
        self.score += self.click_multiplier  # Adiciona o valor do multiplicador
        self.score_label.config(text=f"Pontos: {self.score}")

        # Reinicia o timer para continuar o clique rápido
        self.fast_mode_timer = self.master.after(10, self.fast_click)

    def update_shop_info(self):
        self.score_label.config(text=f"Pontos: {self.score}")
        self.shop_info_label.config(text=f"Custo do Item: {self.item_cost} Pontos\nMultiplicador: {self.click_multiplier}x")

    def update_auto_clicker_info(self):
        self.auto_clicker_info_label.config(text=f"Custo do Auto Clique: {self.auto_clicker_cost} Pontos\nAuto Clicadores: {self.auto_clickers}")

    def update_cps_upgrade_info(self):
        self.cps_upgrade_info_label.config(text=f"Custo do Upgrade de CPS: {self.cps_upgrade_cost} Pontos")

    def update_cps(self):
        # Adiciona pontos de acordo com o número de auto clicadores e o multiplicador de CPS
        self.score += self.auto_clickers * self.cps_multiplier
        self.score_label.config(text=f"Pontos: {self.score}")

        # Atualiza e mostra o CPS
        total_cps = self.clicks_this_second + (self.auto_clickers * self.cps_multiplier)
        self.cps_label.config(text=f"Cliques por Segundo: {total_cps}")
        self.clicks_this_second = 0  # Reseta o contador de cliques

        self.master.after(1000, self.update_cps)  # Chama a função novamente a cada segundo

    def reset_score(self):
        self.score = 0
        self.click_multiplier = 1000  # Reinicia em 1000
        self.item_cost = 10
        self.auto_clickers = 0
        self.auto_clicker_cost = 50
        self.clicks_this_second = 0
        self.cps_multiplier = 1
        self.cps_upgrade_cost = 100
        self.fast_mode = False
        self.stop_fast_mode()  # Para o modo rápido ao reiniciar
        self.score_label.config(text="Pontos: 0")
        self.update_shop_info()
        self.update_auto_clicker_info()
        self.update_cps_upgrade_info()
        self.cps_label.config(text="Cliques por Segundo: 0")
        self.fast_mode_button.config(text="Ativar Auto Clique Rápido")

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()
