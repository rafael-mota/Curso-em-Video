num = int(input('Digite um número: '))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print(f'O número escolhido foi {num}')
#print(f'Unidade: {num[3]}')
#print(f'Dezena: {num[2]}')
#print(f'Centena: {num[1]}')
#print(f'Milhar: {num[0]}')
print(f'Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar: {m}')
