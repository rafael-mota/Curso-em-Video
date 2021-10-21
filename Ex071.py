# SIMULADOR DE CAIXA ELETRÔNICO
print(">>> SIMULADOR DE CAIXA ELETRÔNICO <<<")
contador1 = contador2 = contador5 = contador10 = contador20 = contador50 = contador100 = 0
while True:
    valor_solicitado = int(input("Qual o valor que você deseja sacar? R$"))
    valor = valor_solicitado
    while valor_solicitado != 0:
        if valor_solicitado >= 100:
            valor_solicitado -= 100
            contador100 += 1
            print(valor_solicitado)
        elif valor_solicitado >= 50:
            valor_solicitado -= 50
            contador50 += 1
        elif valor_solicitado >= 20:
            valor_solicitado -= 20
            contador20 += 1
        elif valor_solicitado >= 10:
            valor_solicitado -= 10
            contador10 += 1
        elif valor_solicitado >= 5:
            valor_solicitado -= 5
            contador5 += 1
        elif valor_solicitado >= 2:
            valor_solicitado -= 2
            contador2 += 1
        elif valor_solicitado >= 1:
            valor_solicitado -= 1
            contador1 += 1
    if valor_solicitado == 0:
        break
print(f"Valor de R${valor:.2f} disponibilizado em:")
if contador100 > 0:
    print(f"{contador100} cédulas de R$100.")
if contador50 > 0:
    print(f"{contador50} cédulas de R$50.")
if contador20 > 0:
    print(f"{contador20} cédulas de R$20.")
if contador10 > 0:
    print(f"{contador10} cédulas de R$10.")
if contador5 > 0:
    print(f"{contador5} cédulas de R$5.")
if contador2 > 0:
    print(f"{contador2} cédulas de R$2.")
if contador1 > 0:
    print(f"{contador1} cédulas de R$1.")
