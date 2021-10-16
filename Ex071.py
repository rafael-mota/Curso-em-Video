# SIMULADOR DE CAIXA ELETRÔNICO
print(">>> SIMULADOR DE CAIXA ELETRÔNICO <<<")
contador1 = contador2 = contador5 = contador10 = contador20 = contador50 = contador100 = 0
total = 0
while True:
    valor_solicitado = int(input("Qual o valor que você deseja sacar? R$"))
    while total != valor_solicitado:
        print(total)
        if valor_solicitado % 100 == 0:
            total += 100
            contador100 += 1
        elif valor_solicitado % 50 == 0:
            total += 50
            contador50 += 1
        elif valor_solicitado % 20 == 0:
            total += 20
            contador20 += 1
        elif valor_solicitado % 10 == 0:
            total += 10
            contador10 += 1
        elif valor_solicitado % 5 == 0:
            total += 5
            contador5 += 1
        elif valor_solicitado % 2 == 0:
            total += 2
            contador2 += 1
        elif valor_solicitado % 1 == 0:
            total += 1
            contador1 += 1
    if total % valor_solicitado == 0:
        break

print(f"Valor de R${total:.2f} disponibilizado em:")
if contador100 > 0:
    print(f"{contador100} cédulas de R$100 disponibilizadas:")
if contador50 > 0:
    print(f"{contador50} cédulas de R$50 disponibilizadas:")
if contador20 > 0:
    print(f"{contador20} cédulas de R$20 disponibilizadas:")
if contador10 > 0:
    print(f"{contador10} cédulas de R$10 disponibilizadas:")
if contador5 > 0:
    print(f"{contador5} cédulas de R$5 disponibilizadas:")
if contador2 > 0:
    print(f"{contador2} cédulas de R$2 disponibilizadas:")
if contador1 > 0:
    print(f"{contador1} cédulas de R$1 disponibilizadas:")
