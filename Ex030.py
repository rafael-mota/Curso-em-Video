num = int(input('Insira um número e descubra se ele é par ou ímpar: '))
if num == 0:
    print('Reinicie o programa e digite um número de 1 para cima!')
elif num % 2 == 0:
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é ímpar!')

#Guanabara Code
resultado = num % 2
if resultado == 0:
    print(f'O número {num} é PAR!!!')
else:
    print(f'O numero {num} é IMPAR!!!')
