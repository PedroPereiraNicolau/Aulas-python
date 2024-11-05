def calcular_imposto(salario,aliquota):
    if salario < 0:
        raise ValueError("O salário não pode ser negativo!")
    if aliquota < 0 or aliquota > 1:
        raise ValueError("A aliquota deve ser entre 0 e 1!")
    
    return (salario-100) * aliquota

