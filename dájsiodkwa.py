import pygame
import sys
import math
import random

# Inicializa o Pygame
pygame.init()

# Define as constantes
LARGURA = 800
ALTURA = 600
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

# Configura a tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Plataforma 2D")

# Configura o relógio
clock = pygame.time.Clock()

# Classe do projétil
class Projetil:
    def __init__(self, x, y, direcao):
        self.imagem = pygame.Surface((10, 5))
        self.imagem.fill(VERMELHO)
        self.rect = self.imagem.get_rect(center=(x, y))
        self.velocidade = 10
        self.direcao = direcao

    def mover(self):
        self.rect.x += self.velocidade * self.direcao[0]
        self.rect.y += self.velocidade * self.direcao[1]

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)

# Classe do jogador
class Jogador:
    def __init__(self):
        self.imagem = pygame.Surface((50, 50))
        self.imagem.fill(PRETO)
        self.rect = self.imagem.get_rect()
        self.rect.x = 100
        self.rect.y = ALTURA - 150
        self.velocidade_y = 0
        self.gravidade = 0.5
        self.pode_pular = True

    def mover(self, chaves):
        if chaves[pygame.K_a]:  # Move para a esquerda
            self.rect.x -= 5
        if chaves[pygame.K_d]:  # Move para a direita
            self.rect.x += 5
        if chaves[pygame.K_w] and self.pode_pular:  # Pula
            self.velocidade_y = -10
            self.pode_pular = False

        # Aplicar gravidade
        self.velocidade_y += self.gravidade
        self.rect.y += self.velocidade_y

        # Checando se o jogador está no chão
        if self.rect.y >= ALTURA - 50:
            self.rect.y = ALTURA - 50
            self.velocidade_y = 0
            self.pode_pular = True

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)

# Classe do inimigo
class Inimigo:
    def __init__(self, x, y):
        self.imagem = pygame.Surface((40, 40))
        self.imagem.fill(VERDE)
        self.rect = self.imagem.get_rect(center=(x, y))
        self.velocidade = 2  # Velocidade do inimigo

    def mover(self, jogador):
        # Move em direção ao jogador
        if jogador.rect.x < self.rect.x:
            self.rect.x -= self.velocidade
        elif jogador.rect.x > self.rect.x:
            self.rect.x += self.velocidade

        if jogador.rect.y < self.rect.y:
            self.rect.y -= self.velocidade
        elif jogador.rect.y > self.rect.y:
            self.rect.y += self.velocidade

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)

# Função principal do jogo
def main():
    jogador = Jogador()
    projetis = []
    inimigos = []
    onda_atual = 1
    tempo_onda = 0
    max_inimigos = 3  # Menos inimigos por onda

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Botão esquerdo do mouse
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Calcula a direção para o cursor
                direcao_x = mouse_x - jogador.rect.centerx
                direcao_y = mouse_y - jogador.rect.centery
                magnitude = math.sqrt(direcao_x ** 2 + direcao_y ** 2)
                
                if magnitude > 0:
                    # Normaliza a direção
                    direcao_x /= magnitude
                    direcao_y /= magnitude
                    # Cria um novo projétil na posição do jogador
                    projetil = Projetil(jogador.rect.centerx, jogador.rect.centery, (direcao_x, direcao_y))
                    projetis.append(projetil)

        chaves = pygame.key.get_pressed()
        jogador.mover(chaves)

        # Atualiza a posição dos projéteis
        for proj in projetis[:]:
            proj.mover()
            if (proj.rect.x > LARGURA or proj.rect.x < 0 or 
                proj.rect.y < 0 or proj.rect.y > ALTURA):
                projetis.remove(proj)

        # Atualiza inimigos e checa colisões
        for inimigo in inimigos[:]:
            inimigo.mover(jogador)  # Faz o inimigo se mover em direção ao jogador
            if inimigo.rect.colliderect(jogador.rect):
                print("Game Over!")  # Colisão com o jogador (game over)
                pygame.quit()
                sys.exit()

            for proj in projetis[:]:
                if proj.rect.colliderect(inimigo.rect):
                    projetis.remove(proj)
                    inimigos.remove(inimigo)
                    break

        # Lógica de ondas de inimigos
        tempo_onda += 1
        if tempo_onda >= 60:  # 1 segundo
            for _ in range(max_inimigos + onda_atual):
                x = random.randint(600, 780)  # Posiciona inimigos à direita da tela
                y = random.randint(50, ALTURA - 50)
                inimigos.append(Inimigo(x, y))

            onda_atual += 1
            tempo_onda = 0

        # Preencher a tela com branco
        tela.fill(BRANCO)
        jogador.desenhar(tela)

        # Desenha os projéteis
        for proj in projetis:
            proj.desenhar(tela)

        # Desenha os inimigos
        for inimigo in inimigos:
            inimigo.desenhar(tela)

        # Atualizar a tela
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
