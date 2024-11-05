import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Programação Monstros")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Classe para Linguagens de Programação
class Language:
    def __init__(self, name, attack_power):
        self.name = name
        self.hp = 100
        self.attack_power = attack_power

    def attack(self):
        return random.randint(0, self.attack_power)

# Criando as linguagens
languages = [
    Language("Python", 40),
    Language("Java", 35),
    Language("JavaScript", 45),
    Language("C++", 50),
    Language("Ruby", 40)
]

# Função para escolher uma linguagem aleatória do rival
def choose_opponent():
    return random.choice(languages)

# Função principal do jogo
def main():
    clock = pygame.time.Clock()
    running = True

    player_language = languages[0]  # Você escolhe Python
    opponent_language = choose_opponent()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Exibir informações do jogador
        font = pygame.font.Font(None, 36)
        player_text = font.render(f"{player_language.name} HP: {player_language.hp}", True, BLACK)
        opponent_text = font.render(f"{opponent_language.name} HP: {opponent_language.hp}", True, BLACK)
        
        screen.blit(player_text, (50, 50))
        screen.blit(opponent_text, (50, 100))

        # Simulação de ataque
        if opponent_language.hp > 0:
            attack_damage = player_language.attack()
            opponent_language.hp -= attack_damage
            if opponent_language.hp < 0:
                opponent_language.hp = 0

        pygame.display.flip()
        clock.tick(1)  # Limita a 1 atualização por segundo

    pygame.quit()

if __name__ == "__main__":
    main()
