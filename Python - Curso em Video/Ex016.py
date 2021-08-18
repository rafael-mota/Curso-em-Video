#Exibe a porção inteira de um numero real
from math import trunc
num = float(input('Digite um numero real: '))
#Módulo trunc() trunca as casas decimais para transformar o valor do input em um numero inteiro.
print(f'A porção inteira de {num} é {trunc(num)}')