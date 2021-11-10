#Separação de valores pares e ímpares em lista
lista = [list(), list()]
for i in range(7):
    num = int(input(f"Digite o {i + 1}º valor: "))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f"A lista completa é {lista}")
print(f"Os números pares da lista são {lista[0]}")
print(f"Os números ímpares da lista são {lista[1]}")