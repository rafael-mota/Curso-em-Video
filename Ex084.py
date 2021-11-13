#Analise de dados - Pessoa x Peso
pessoa = []
lista_pessoas = []
acima_do_peso = []
abaixo_do_peso = []
while True:
    pessoa.append(str(input("Nome: ")))
    pessoa.append(float(input("Peso: ")))
    lista_pessoas.append(pessoa[:])
    if len(acima_do_peso) == 0 and len(abaixo_do_peso) == 0:
        acima_do_peso.append(pessoa[:])
        abaixo_do_peso.append(pessoa[:])
    else:
        if pessoa[1] >= acima_do_peso[-1][-1]:
            acima_do_peso.append(pessoa[:])
        elif pessoa[1] <= abaixo_do_peso[-1][-1]:
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
    if p[1] == acima_do_peso[-1][-1]:
        print(p[0], end=" ")
print(f"\nO menor peso foi de {abaixo_do_peso[-1][-1]}. Peso de", end=" ")
for p in abaixo_do_peso:
    if p[1] == abaixo_do_peso[-1][-1]:
        print(p[0], end=" ")
