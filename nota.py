print("Digite as notas entre 0 e 10")
numero1 = int(input())    
numero2 = int(input())
numero3 = int(input())
numero4 = int(input())
nota = [numero1,numero2,numero3,numero4]

resultado = (nota[0] + nota[1] + nota[2]+ nota[3]) / 4
if resultado > 5:
    print("Aprovado sua media é",resultado)
elif resultado >= 3 and resultado <= 5:
    print("Recuperação sua media é",resultado)
elif resultado < 3:
    print("Reprovado sua media é",resultado)
else:
    print("Digite certo")