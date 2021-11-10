#Analise de dados - Pessoa x Peso
pessoa = []
lista_pessoas = []
acima_do_peso = []
abaixo_do_peso = []

while True:
    pessoa.append(str(input("Nome: ")))
    pessoa.append(float(input("Peso: ")))
    lista_pessoas.append(pessoa[:])
    if pessoa[1] >= 100:
        acima_do_peso.append(pessoa[:])
    elif pessoa[1] <= 70:
        abaixo_do_peso.append(pessoa[:])
    pessoa.clear()
    continuar = " "
    while continuar not in "SsNn":
        continuar = str(input("Deseja continuar? [S/N] >>> ")).strip()[0]
    if continuar in "Nn":
        break
print(f"{len(lista_pessoas)} pessoas foram cadastradas ao todo.")
print(f"O maior peso foi de {acima_do_peso[-1][-1]}. Peso de", end=" ")
for p in acima_do_peso:
     print(p[0], end=" ")
print(f"\nO menor peso foi de {abaixo_do_peso[-1][-1]}. Peso de", end=" ")
for p in abaixo_do_peso:
     print(p[0], end=" ")