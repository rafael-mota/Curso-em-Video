#Conversão de valor para binario, octal e hexadecimal.
valor = int(input('Insira um número inteiro para conversão: '))
conver = int(input('Para qual valor deseja converter? \n1 - Binário \n2 - Octal \n3 - Hexadecimal \n>>> '))
if conver == 1:
    print(f'O valor {valor} convertido em BINÁRIO é {valor:b}')
elif conver == 2:
    print(f'O valor {valor} convertido em OCTAL é: {valor:o}')
elif conver == 3:
    print(f'O valor {valor} convertido em HEXADECIMAL é: {valor:x}')
else:
    print('Retorne o processo e insira um número de 1 à 3')