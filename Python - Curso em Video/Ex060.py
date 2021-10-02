#NUMERO FATORIAL WHILE
print("Descubra o valor FATORIAL de um numero")
numero = int(input("Insira o número: "))
count = 1
fatorial = 1
while count != numero:
    fatorial += fatorial * count
    count += 1
print(f"O {numero}! é {fatorial}")

#NUMERO FATORIAL FOR