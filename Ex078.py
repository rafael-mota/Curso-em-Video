#Check de valores - MAIOR E MENOR COM INPUT
lista = []
minimo = 0
maximo = 0
indice_min = []
indice_max = []
for posicao in range(5):
    lista.append(int(input(f"Digite um valor para a posição {posicao}: ")))
for indice, valor in enumerate(lista):
    if minimo == 0 and maximo == 0:
       minimo = maximo = valor
       indice_max.append(indice)
       indice_min.append(indice)
    elif valor < minimo:
        minimo = valor
        indice_min.clear()
        indice_min.append(indice)
    elif valor > maximo:
        maximo = valor
        indice_max.clear()
        indice_max.append(indice)
    elif valor == minimo:
        indice_min.append(indice)
    elif valor == maximo:
        indice_max.append(indice)
print(f"Você digitou os valores {lista}")
print(f"O maior valor da lista foi {maximo} e está no indice", end=" ")
for index in indice_max:
    print(f"{index}...", end=" ")
print(f"\nO menor valor da lista foi {minimo} e está no indice", end=" ")
for index in indice_min:
    print(f"{index}...", end=" ")