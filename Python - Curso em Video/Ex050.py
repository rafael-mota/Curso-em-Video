count = 0
soma = 0
for i in range(6):
    num = int(input("Insira um número inteiro: "))
    if num % 2 == 0:
        count += num
        soma += 1
print(f'Você digitou {soma} números pares. A soma total deles é {count}')
print('FIM')
