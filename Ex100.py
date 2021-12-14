#Lista com numeros aleatórios e funções
from random import randint
from time import sleep


numeros = list()


def sorteia():
    print("Sorteando 5 valores para lista:", end=' ')
    for i in range(5):
        numeros.append(randint(0, 10))
        print(numeros[i], end=' ')
        sleep(0.3)
    print("PRONTO!")


def somapar():
    soma = 0
    for p in numeros:
        if p % 2 == 0:
            soma += p
    print(f"Somando os valores pares de {numeros}, temos {soma}")

sorteia()
somapar()