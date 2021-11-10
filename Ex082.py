#Analise de numeros pares e impares em listas com condicionais e looping.
lista = []
lista_par = []
lista_impar = []
lista_par_for = []
lista_impar_for = []

while True:
    num = (int(input("Digite um número para ser adicionado a lista: ")))
    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    elif num % 2 == 1:
        lista_impar.append(num)

    continuar = " "
    while continuar not in "SsNn":
        continuar = str(input("Deseja continuar? [S/N] >>> ")).strip()[0]
    if continuar in "Nn":
        break

print(f"A lista completa é {lista}")
print(f"A lista de pares é {lista_par}")
print(f"A lista de ímpares é {lista_impar}")

for i in lista:
    if i % 2 == 0:
        lista_par_for.append(i)
    elif i % 2 == 1:
        lista_impar_for.append(i)

print(f"A lista de pares utilizando for é {lista_par_for}")
print(f"A lista de ímpares utilizando for é {lista_impar_for}")
