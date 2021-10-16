nome = input('Digite seu nome completo: ')
nome2 = nome.split()
nome3 = (''.join(nome2))
print(nome.upper())
print(nome.lower())
# teste print(nome2)
print(f'Seu nome completo tem ao todo {len(nome3)} letras')
#Podemos usar a função (len(nome) - nome.count('')) para contar quantas letras o nome completo tem excluindo os espaços!
print(f'O primeiro nome tem {len(nome2[0])} letras')