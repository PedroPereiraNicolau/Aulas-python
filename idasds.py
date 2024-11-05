import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo da Forca")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonte
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Lista de palavras
palavras = ["python", "programa", "desafio", "computador", "jogo"]

def escolher_palavra():
    return random.choice(palavras)

def desenhar_palavra(palavra, letras_adivinhadas):
    return " ".join([letra if letra in letras_adivinhadas else "_" for letra in palavra])

def desenhar_enforcado(tentativas):
    base_x = 150
    base_y = 200

    if tentativas < 6:
        pygame.draw.circle(screen, BLACK, (base_x, base_y), 20)  # Cabeça
    if tentativas < 5:
        pygame.draw.line(screen, BLACK, (base_x, base_y + 20), (base_x, base_y + 120), 5)  # Corpo
    if tentativas < 4:
        pygame.draw.line(screen, BLACK, (base_x, base_y + 40), (base_x - 50, base_y + 80), 5)  # Braço esquerdo
    if tentativas < 3:
        pygame.draw.line(screen, BLACK, (base_x, base_y + 40), (base_x + 50, base_y + 80), 5)  # Braço direito
    if tentativas < 2:
        pygame.draw.line(screen, BLACK, (base_x, base_y + 120), (base_x - 50, base_y + 180), 5)  # Perna esquerda
    if tentativas < 1:
        pygame.draw.line(screen, BLACK, (base_x, base_y + 120), (base_x + 50, base_y + 180), 5)  # Perna direita

def mostrar_mensagem(mensagem):
    resultado_surface = small_font.render(mensagem, True, BLACK)
    screen.blit(resultado_surface, (screen_width // 2 - resultado_surface.get_width() // 2, screen_height // 2 - 20))

def desenhar_botao(texto, x, y, largura, altura, cor_normal, cor_hover):
    mouse = pygame.mouse.get_pos()
    if x < mouse[0] < x + largura and y < mouse[1] < y + altura:
        pygame.draw.rect(screen, cor_hover, (x, y, largura, altura))
    else:
        pygame.draw.rect(screen, cor_normal, (x, y, largura, altura))
    
    botao_surface = small_font.render(texto, True, WHITE)
    screen.blit(botao_surface, (x + (largura - botao_surface.get_width()) // 2, y + (altura - botao_surface.get_height()) // 2))

def main():
    while True:
        palavra = escolher_palavra()
        letras_adivinhadas = []
        tentativas = 6
        game_over = False

        while True:
            screen.fill(WHITE)

            # Verifica se o jogo acabou
            if game_over:
                resultado_texto = "Você ganhou!" if "_" not in desenhar_palavra(palavra, letras_adivinhadas) else f"Você perdeu! A palavra era: {palavra}"
                mostrar_mensagem(resultado_texto)

                # Desenha botões
                desenhar_botao("Reiniciar", 200, 500, 150, 50, GREEN, (0, 200, 0))
                desenhar_botao("Sair", 450, 500, 150, 50, RED, (200, 0, 0))

                # Verifica cliques
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 200 < event.pos[0] < 350 and 500 < event.pos[1] < 550:  # Reiniciar
                            break  # Reinicia o loop principal
                        if 450 < event.pos[0] < 600 and 500 < event.pos[1] < 550:  # Sair
                            pygame.quit()
                            sys.exit()
            else:
                # Desenha a palavra
                palavra_oculta = desenhar_palavra(palavra, letras_adivinhadas)
                palavra_surface = font.render(palavra_oculta, True, BLACK)
                screen.blit(palavra_surface, (screen_width // 2 - palavra_surface.get_width() // 2, screen_height // 2 - 100))

                # Mostra tentativas restantes
                tentativas_surface = small_font.render(f"Tentativas restantes: {tentativas}", True, BLACK)
                screen.blit(tentativas_surface, (screen_width // 2 - tentativas_surface.get_width() // 2, screen_height // 2 + 20))

                # Desenha o enforcado
                desenhar_enforcado(tentativas)

                # Mostra letras já adivinhadas
                letras_surface = small_font.render("Letras já tentadas: " + " ".join(letras_adivinhadas), True, BLACK)
                screen.blit(letras_surface, (20, screen_height - 50))

            # Atualiza a tela
            pygame.display.flip()

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and not game_over:
                    if event.unicode.isalpha() and len(event.unicode) == 1:
                        letra = event.unicode.lower()
                        if letra not in letras_adivinhadas:
                            letras_adivinhadas.append(letra)
                            if letra not in palavra:
                                tentativas -= 1

                            if "_" not in desenhar_palavra(palavra, letras_adivinhadas) or tentativas <= 0:
                                game_over = True

        # Reinicia o jogo com uma nova palavra
        continue  # Reinicia o loop principal com nova palavra

if __name__ == "__main__":
    main()
