#TRATAMENTO DE VALORES COM FLAG
num = int(input("DIGITE UM NÚMERO *DIGITE 999 PARA PARAR* >>> "))
count = soma = 0
while num != 999:
    count += 1
    soma += num
    num = int(input("DIGITE UM NÚMERO *DIGITE 999 PARA PARAR* >>> "))
print(f"Você digitou {count} números e a soma deles foi {soma}")
