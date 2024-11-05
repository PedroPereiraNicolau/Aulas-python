print("Digite 2 numeros e eu vou dizer qual é maior")

num1 = int(input())
num2 = int(input())

if num1 > num2:
    print("O primeiro numero é maior")
elif num2 > num1:
    print("O segundo numero é maior")
elif num1 == num2:
    print("Os numeros sao iguais")
else:
    print("Digitou errado")