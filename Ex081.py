#Analise de dados com listas
lista = []
while True:
    lista.append(int(input("Insira um número para inserir na lista: ")))
    continuar = " "
    while continuar not in "SsNn":
        continuar = str(input("Deseja continuar? [S/N] >>> ")).strip()[0]
    if continuar in "Nn":
        break
print(f"Você digitou {len(lista)} elementos.")
lista.sort(reverse=True)
print(f"Os valores em ordem descrescente são {lista}")
if 5 in lista:
    print("O valor 5 CONSTA da lista!")
else:
    print("O valor 5 NÃO CONSTA na lista.")
