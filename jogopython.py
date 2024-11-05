import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela em 800x600
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Programação Monstros")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Classe para Linguagens de Programação
class Language:
    def __init__(self, name, attacks, image_path):
        self.name = name
        self.hp = 100
        self.attacks = attacks
        self.image_path = image_path
        self.image = pygame.image.load(image_path)

    def attack(self):
        attack_index = random.randint(0, len(self.attacks) - 1)
        attack_line = self.attacks[attack_index]['name']
        base_damage = random.randint(10, 15)

        if random.random() < 0.2:
            base_damage *= 2
            attack_line += " (Crítico!)"

        return attack_line, base_damage

# Criando as linguagens com seus ataques e imagens
languages = [
    Language("Python", [
        {'name': 'print("Hello, World!")'},
        {'name': 'import random'},
        {'name': 'def func(): return "Python"'},
        {'name': 'for i in range(5): print(i)'}
    ], "images/python.png"),
    
    Language("Java", [
        {'name': 'System.out.println("Hello, World!");'},
        {'name': 'public void run() { /*...*/ }'},
        {'name': 'int x = 5;'},
        {'name': 'if (x > 0) { /*...*/ }'}
    ], "images/java.png"),
    
    Language("JavaScript", [
        {'name': 'console.log("Hello, World!");'},
        {'name': 'let x = 10;'},
        {'name': 'fetch("url").then(response => response.json());'},
        {'name': 'for(let i = 0; i < 5; i++) { console.log(i); }'}
    ], "images/javascript.png"),
    
    Language("Ruby", [
        {'name': 'puts "Hello, World!"'},
        {'name': 'x = 10'},
        {'name': '5.times { puts "Ruby" }'},
        {'name': 'require "json"'}
    ], "images/ruby.png")
]

# Função para a tela inicial
def main_menu():
    font = pygame.font.Font(None, 48)
    running = True

    while running:
        screen.fill(WHITE)
        title_text = font.render("Programação Monstros", True, BLACK)
        casual_text = font.render("Pressione C para Luta Casual", True, BLACK)
        tournament_text = font.render("Pressione T para Torneio", True, BLACK)

        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 100))
        screen.blit(casual_text, (screen_width // 2 - casual_text.get_width() // 2, 200))
        screen.blit(tournament_text, (screen_width // 2 - tournament_text.get_width() // 2, 250))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    casual_battle()
                    running = False
                elif event.key == pygame.K_t:
                    tournament()
                    running = False

# Função para a luta casual
def casual_battle():
    selected_languages = choose_languages()
    player_language, opponent_language = selected_languages
    battle(player_language, opponent_language)

# Função para escolher as linguagens
def choose_languages():
    font = pygame.font.Font(None, 36)
    running = True
    selected_languages = []

    while running:
        screen.fill(WHITE)
        title_text = font.render("Escolha 2 linguagens:", True, BLACK)
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 50))

        for i, lang in enumerate(languages):
            lang_text = font.render(f"{i + 1}: {lang.name}", True, BLACK)
            screen.blit(lang_text, (screen_width // 2 - lang_text.get_width() // 2, 100 + i * 40))
            if lang in selected_languages:
                pygame.draw.rect(screen, BLACK, (screen_width // 2 - 130, 100 + i * 40, 20, 20))

        instructions = font.render("Pressione 1, 2, 3 ou 4 para selecionar, ESC para confirmar.", True, BLACK)
        screen.blit(instructions, (screen_width // 2 - instructions.get_width() // 2, screen_height - 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    index = event.key - pygame.K_1
                    lang = languages[index]
                    if lang not in selected_languages:
                        selected_languages.append(lang)
                    if len(selected_languages) == 2:
                        running = False

        pygame.display.flip()

    return selected_languages

# Função para jogar o torneio
def tournament():
    random.shuffle(languages)
    winners = []

    for i in range(0, len(languages), 2):
        if i + 1 < len(languages):
            # Resetar a vida das linguagens antes da batalha
            languages[i].hp = 100
            languages[i + 1].hp = 100
            winner = battle(languages[i], languages[i + 1])
            winners.append(winner)

    if len(winners) == 2:
        # Resetar a vida das linguagens na final
        winners[0].hp = 100
        winners[1].hp = 100
        final_winner = battle(winners[0], winners[1])
        show_result(final_winner, winners[0], winners[1])
    else:
        print("Não há oponentes suficientes para a final!")

def battle(player_language, opponent_language):
    clock = pygame.time.Clock()
    running = True
    player_turn = True
    message = ""
    attack_delay = 1000  # Intervalo de 1 segundo
    last_attack_time = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = pygame.time.get_ticks()

        if player_language.hp > 0 and opponent_language.hp > 0:
            if current_time - last_attack_time >= attack_delay:
                if player_turn:
                    attack_line, attack_damage = player_language.attack()
                    opponent_language.hp -= attack_damage
                    message = f"{player_language.name} usou {attack_line} causando {attack_damage} de dano!"
                else:
                    attack_line, attack_damage = opponent_language.attack()
                    player_language.hp -= attack_damage
                    message = f"{opponent_language.name} usou {attack_line} causando {attack_damage} de dano!"

                player_turn = not player_turn
                last_attack_time = current_time

        screen.fill(WHITE)

        font = pygame.font.Font(None, 36)
        player_text = font.render(f"{player_language.name} HP: {player_language.hp}", True, BLACK)
        opponent_text = font.render(f"{opponent_language.name} HP: {opponent_language.hp}", True, BLACK)

        screen.blit(player_text, (50, 50))
        screen.blit(opponent_text, (screen_width - 250, 50))

        if message:
            wrapped_message = text_wrap(message, font, screen_width - 100)
            for i, line in enumerate(wrapped_message):
                message_text = font.render(line, True, BLACK)
                screen.blit(message_text, (50, 400 + i * 30))

        screen.blit(player_language.image, (50, 100))
        screen.blit(opponent_language.image, (screen_width - 200, 100))

        if player_turn:
            attack_message = font.render(f"{player_language.name} atacou!", True, BLACK)
            screen.blit(attack_message, (50, 250))
        else:
            attack_message = font.render(f"{opponent_language.name} atacou!", True, BLACK)
            screen.blit(attack_message, (screen_width - 250, 250))

        if player_language.hp <= 0:
            message = f"{player_language.name} foi derrotado!"
            running = False
            return opponent_language
        elif opponent_language.hp <= 0:
            message = f"{opponent_language.name} foi derrotado!"
            running = False
            return player_language

        pygame.display.flip()
        clock.tick(30)

def text_wrap(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        if font.size(current_line + word)[0] < max_width:
            current_line += word + " "
        else:
            lines.append(current_line)
            current_line = word + " "

    lines.append(current_line)
    return lines

def show_result(winner, player_language, opponent_language):
    font = pygame.font.Font(None, 48)
    running = True

    while running:
        screen.fill(WHITE)
        result_text = font.render(f"{winner.name} venceu!", True, BLACK)
        replay_text = font.render("Pressione R para jogar novamente ou ESC para sair", True, BLACK)

        screen.blit(result_text, (screen_width // 2 - result_text.get_width() // 2, screen_height // 2 - 50))
        screen.blit(replay_text, (screen_width // 2 - replay_text.get_width() // 2, screen_height // 2 + 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main_menu()  # Voltar ao menu inicial
                    running = False
                elif event.key == pygame.K_ESCAPE:
                    running = False

def main():
    main_menu()  # Inicia o menu principal

if __name__ == "__main__":
    main()
