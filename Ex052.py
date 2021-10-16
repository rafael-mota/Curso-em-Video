#NUMERO PRIMO
count = 0
num = int(input("Digite um número: "))
for i in range(1, num + 1):
    if num % i == 0 or num % i == num:
        print(f"\033[1;32m{i}\033[m", end=' ')
        count += 1
    else:
        print(f"\033[1;31m{i}\033[m", end=' ')
if count == 2:
    print(f'\nO número {num} foi divisível {count} vezes! \nE por isso ele é PRIMO!')
else:
    print(f'\nO número {num} foi divisível {count} vezes! \nE por isso ele NÃO É PRIMO!')
    