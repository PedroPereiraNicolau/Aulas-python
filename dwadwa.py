import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokémon Game")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Classe para o Pokémon
class Pokemon:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

# Função principal do jogo
def main():
    clock = pygame.time.Clock()
    
    # Exemplo de Pokémon
    bulbasaur = Pokemon("Bulbasaur", 100, 10)
    pikachu = Pokemon("Pikachu", 100, 12)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)

        # Exibir informações do Pokémon
        font = pygame.font.Font(None, 36)
        text = font.render(f"{bulbasaur.name}: {bulbasaur.health} HP", True, BLACK)
        screen.blit(text, (50, 50))

        text = font.render(f"{pikachu.name}: {pikachu.health} HP", True, BLACK)
        screen.blit(text, (50, 100))

        pygame.display.flip()
        clock.tick(60)

# Iniciar o jogo
if __name__ == "__main__":
    main()
