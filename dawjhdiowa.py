# Dicionário para armazenar os livros
livros = {}

# Função para adicionar livros ao dicionário
def adicionar_livro():
    while True:
        codigo = int(input("Digite o código do livro (um número inteiro único): "))
        # Verifica se o código já existe no dicionário
        if codigo in livros:
            print("\nErro: O código já foi utilizado! Digite um código único.\n")
        else:
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = int(input("Digite o ano de publicação do livro: "))
            
            # Adiciona o livro ao dicionário
            livros[codigo] = {"titulo": titulo, "autor": autor, "ano": ano}
            print(f"\nLivro '{titulo}' adicionado com sucesso!\n")
            break  # Encerra o loop após adicionar o livro com um código único

# Função para procurar livro pelo código
def procurar_por_codigo(codigo):
    if codigo in livros:
        livro = livros[codigo]
        print(f"\nInformações do livro com código {codigo}:")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano de publicação: {livro['ano']}")
    else:
        print("\nLivro não encontrado!")

# Função principal para interagir com o usuário
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar um livro")
        print("2. Procurar livro por código")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_livro()
        elif opcao == '2':
            try:
                codigo = int(input("Digite o código do livro que deseja procurar: "))
                procurar_por_codigo(codigo)
            except ValueError:
                print("\nErro: Por favor, digite um código válido (número inteiro).\n")
        elif opcao == '3':
            print("\nSaindo... Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

# Executa o menu
menu()
