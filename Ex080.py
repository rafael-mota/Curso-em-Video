#Inserção de valores em lista em ordem crescente sem sort()
lista = []
while len(lista) != 5:
    num = (int(input("Digite um valor para adicionar a lista (Ordem crescente): ")))
    if len(lista) == 0 or num > lista[len(lista) - 1]:
        lista.append(num)
        print("Valor inserido no final da lista.")
    else:
        for i in lista:
            if lista.count(num) > 1:
                print("Valor previamente informado não será inserido na lista.")
                break
            elif num < i:
                lista.insert((lista.index(i)), num)
                print(f"Valor adicionado ao indice {lista.index(num)} da lista.")
                break
            elif num > i:
                lista.insert((lista.index(i)) + 1, num)
                print(f"Valor adicionado ao indice {lista.index(num)} da lista.")
                break
print(f"Os valores digitados em ordem foram: {lista}")