from calculoimposto import calcular_imposto

def main():
    try:
        #Recebe o salário e a aliquota do usuário
        salario = float(input("Digite o salário:"))
        aliquota = float(input("Digite a aliquota(por exemplo 0,1.):"))

        #Calcula o imposto
        imposto = calcular_imposto(salario,aliquota)
        print(f"O imposto sobre o salário de R${salario}com uma aliquota de {aliquota*100}% é R${imposto:.2f}.")

    except ValueError as e:
        print(f"Erro: {e}")
if __name__ == "__main__":
    main()