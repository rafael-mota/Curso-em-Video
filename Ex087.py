#Analise de dados com matrizes
matriz = []
soma_tc = pares = 0
for linha in range(3):
    matriz.append(list())
    for coluna in range(3):
        num = int(input(f"Digite um valor para [{linha},{coluna}]: "))
        matriz[linha].append(num)
        if num % 2 == 0:
            pares += num
        if coluna == 2:
            soma_tc += num
print("=-="*8)
for i in matriz:
    for valor in i:
        print(f"[  {valor}  ]", end=" ")
    print("\r")
print("=-="*8)
print(f"A soma dos valores pares é {pares}")
print(f"A soma dos valores da terceira coluna é {soma_tc}")
print(f"O maior valor da segunda coluna é {max(matriz[1])}")