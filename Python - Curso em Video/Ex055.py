#MAIOR OU MENOR DA SEQUENCIA
lst = []
for i in range(1, 6):
    peso = float(input(f'Qual o peso da {i}ª pessoa: '))
    lst.insert(i, peso)
lst.sort()
print(f"O maior peso lido foi de: {lst[0]}")
print(f"O menor peso lido foi de: {lst[-1]}")
