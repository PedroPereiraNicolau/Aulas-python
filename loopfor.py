numero = int(input("Digite um numero: "))
soma = 0
for contador in range(1,numero+1):
    soma = soma + contador
    print(f'{soma}+{contador} = {soma}')
print(f"O resultado é: {soma}",)