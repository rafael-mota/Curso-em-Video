#Analisador completo
idcount = 0
fmenor = 0
hmvelho = ""
hmvelhoid = 0
for i in range (1, 5):
    print(f">>> {i}ª PESSOA <<<")
    nome = str(input("Nome: ")).upper().strip()
    idade = int(input("Idade: "))
    sexo = str(input("[M/F]: ")).upper()
    idcount += idade
    if sexo == "F" and idade < 20:
        fmenor += 1
    elif sexo == "M":

hmvelho = nome
hmvelhoid = idade
print(f"A média de idade do grupo é de {idcount / 4}")
print(f"O homem mais velho tem {hmvelhoid} e se chama {hmvelho}")
print(f"Ao todo são {fmenor} mulheres com menos de 20 anos")
