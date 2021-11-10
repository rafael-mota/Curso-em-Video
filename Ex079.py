#Validação de valores em lista
lista = []
while True:
    num = (int(input("Digite um valor para adicionar a lista: ")))
    if lista.count(num) == 0:
        lista.append(num)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não será inserido na lista.")
    continuar = " "
    while continuar not in "SsNn":
        continuar = str(input("Deseja continuar? [S/N] >>> ")).strip()[0]
    if continuar in "Nn":
        break
lista.sort()
print(f"Os valores digitados em ordem foram: {lista}")