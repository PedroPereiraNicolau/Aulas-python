print("Digite as notas entre 0 e 10")  # Solicita ao usuário que digite as notas

nota = []  # Cria uma lista vazia para armazenar as notas

# Loop que se repete 4 vezes para receber 4 notas
for i in range(4):
    while True:  # Inicia um loop que continua até uma entrada válida ser fornecida
        try:
            # Solicita a nota, convertendo a entrada do usuário para um float
            nota_input = float(input(f"Nota {i + 1}: "))
            
            # Verifica se a nota está entre 0 e 10
            if 0 <= nota_input <= 10:
                nota.append(nota_input)  # Adiciona a nota válida à lista
                break  # Sai do loop se a nota for válida
            else:
                print("Por favor, insira uma nota entre 0 e 10.")  # Mensagem de erro se a nota estiver fora do intervalo
        except ValueError:
            # Captura o erro se a entrada não puder ser convertida para float
            print("Entrada inválida. Por favor, insira um número.")  # Mensagem de erro para entradas inválidas

# Calcula a média das notas
resultado = sum(nota) / len(nota)

# Verifica a média para determinar a situação do aluno
if resultado > 5:
    print("Aprovado! Sua média é:", resultado)  # Mensagem para aluno aprovado
elif 3 <= resultado <= 5:
    print("Recuperação! Sua média é:", resultado)  # Mensagem para aluno em recuperação
else:
    print("Reprovado! Sua média é:", resultado)  # Mensagem para aluno reprovado
