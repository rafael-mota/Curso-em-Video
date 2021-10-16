#Menu de opcões
valor_1 = int(input("Insira um valor: "))
valor_2 = int(input("Insira outro valor: "))
menu = '''O que você quer fazer com esse valores?
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA'''
print(menu)
selecao = int(input(">>> "))
while selecao != 5:
    if selecao == 1:
        print(f"A SOMA DE {valor_1} + {valor_2} é igual á: {valor_1 + valor_2}")
    elif selecao == 2:
        print(f"A MULTIPLICAÇÃO DE {valor_1} + {valor_2} é igual á: {valor_1 * valor_2}")
    elif selecao == 3:
        if valor_1 > valor_2:
            print(f"O valor {valor_1} é maior que {valor_2}")
        elif valor_2 > valor_1:
            print(f"O valor {valor_2} é maior que {valor_1}")
        else:
            print(f"Os valores {valor_2} e {valor_1} são iguais!")
    elif selecao == 4:
        print("Por favor, insira novos valores")
        valor_1 = int(input("Insira um valor: "))
        valor_2 = int(input("Insira outro valor: "))
    else:
        print("Insira uma opção válida")
    print(menu)
    selecao = int(input(">>> "))
print("FIM DO PROGRAMA")