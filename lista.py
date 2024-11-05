compras = ["1","2","3","4"]
print(compras[0])

posicao = 0
while posicao < 4:
    print(compras [posicao])
    posicao += 1
print(compras)
compras.append("5")
print(compras)
compras.insert(0,"milho")
print(compras)
compras.sort()
print(compras)
sublista = compras[0:4]
print(sublista)
sublista2 = compras[0:]
print(sublista2)
sublista3 = compras[:4]
print(sublista3)
sublista4 = compras[0-1]
print(sublista4)
quantidade = len(compras)