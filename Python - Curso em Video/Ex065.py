#Analise de valores -> Maior e Menor com média.
print(">>> ANÁLISE DE VALORES <<<")
maior = menor = contador = soma = num = 0
cont = "s"
while cont not in "Nn":
    num = int(input("Digite um número >>> "))
    contador += 1
    soma += num
    #Na primeira condição estabelecemos um valor padrão para todas as variaveis (maior, menor = num)
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    cont = str(input("Deseja continuar? [S/N] >>> ")).strip()[0]
print(f"Você digitou {contador} números e a média foi {soma/contador}")
print(f"O maior valor foi {maior} e o menor foi {menor}.")

