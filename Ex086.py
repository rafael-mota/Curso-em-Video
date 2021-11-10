#Criação de matrizes com listas
matriz = []
for linha in range(3):
    matriz.append(list())
    for coluna in range(3):
        matriz[linha].append(int(input(f"Digite um valor para [{linha},{coluna}]: ")))
print("=-="*8)
for i in matriz:
    for valor in i:
        print(f"[  {valor}  ]", end=" ")
    print("\r")