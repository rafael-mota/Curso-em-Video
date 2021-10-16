nome = str(input('Digite um nome completo: ')).strip()
nomeabr = nome.split()
print(f'O nome digitado foi {nome} \nSeu primeiro nome é {nomeabr[0]} \nE seu último nome é {nomeabr[-1]}')