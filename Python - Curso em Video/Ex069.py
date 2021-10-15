#Cadastro e analise de dados com while

contador_maioridade = 0
contador_masculino = 0
contador_feminino_menor = 0

while True:
    print(">>> CADASTRO PARA ANÁLISE <<<")
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))[0]
    while sexo not in "MmFf":
        sexo = str(input("Sexo [M/F]: "))[0]
    continuar = str(input("Quer continuar? [S/N]: ")).strip()[0]
    while continuar not in "SsNn":
        continuar = str(input("Quer continuar? [S/N]: ")).strip()[0]
    if continuar not in "Ss":
        break
    else:
        if idade >= 18:
            contador_maioridade += 1
        if sexo in "Mm":
            contador_masculino += 1
        elif sexo in "Ff" and idade < 20:
            contador_feminino_menor += 1

print(f"PROCESSO DE CADASTRO ENCERRADO. ")
print(f"{contador_maioridade} pessoas cadastradas tem mais de 18 anos;")
print(f"{contador_masculino} Homens foram cadastrados;")
print(f"{contador_feminino_menor} Mulheres tem menos de 20 anos")
