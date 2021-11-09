#Check de valores - MAIOR E MENOR COM INPUT
lista = []
minimo = 0
indice_min = 0
maximo = 0
indice_max = 0
for valor in range(5):
    lista.append(int(input(f"Digite um valor para a posição {valor}: ")))
for indice, valor in enumerate(lista):
    if minimo == 0 and maximo == 0:
        minimo = maximo = valor
    elif valor < minimo:
        minimo = valor
        indice_min = indice
    elif valor > maximo:
        maximo = valor
        indice_max = indice

print(f"Você digitou os valores {lista}")
print(f"O valor maior valor da lista foi {max(lista)} e está no indice {lista.index(max(lista))}")
print(f"O valor menor valor da lista foi {min(lista)} e está no indice {lista.index(min(lista))}")