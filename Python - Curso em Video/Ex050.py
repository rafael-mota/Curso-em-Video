count = 0
for i in range(6):
    num = int(input("Insira um número inteiro: "))
    if num % 2 == 0:
        count += num
print(count)
print('FIM')