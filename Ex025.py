nome = str(input('Digite seu nome: ')).strip()
sobre = 'Silva'
if sobre in nome:
    print(f'O nome {sobre} consta nesse nome!')
else:
    print(f'O nome {sobre} não consta nesse nome!')

#Outra solução:
print(f'Seu nome tem Silva? {"silva" in nome.lower()}')

