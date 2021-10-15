#Análise de números com FLAG
count = soma = 0
while True:
    num = int(input("Insira um número [Digite 999 para encerrar] >>> "))
    if num == 999:
        break
    count += 1
    soma += num
print(f"A soma total dos {count} números digitados é {soma}")
