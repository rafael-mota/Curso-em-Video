#SOMA DE NÚMEROS ÍMPARES MULTIPLOS DE 3
count = 0
count2 = 0
for i in range(0, 501, 3):
    if i % 2 != 0:
        count += i
        count2 += 1
print(f'A soma de todos os {count2} valores solicitados é: {count}')

#Código otimizado: print(sum(range(3, 501, 6)))