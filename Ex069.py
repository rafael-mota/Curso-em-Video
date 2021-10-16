# Cadastro com análise de dados
contador_maioridade = contador_masculino = contador_feminino_menor = 0

while True:
    print(">>> CADASTRO PARA ANÁLISE <<<")
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MmFf":
        sexo = str(input("Sexo [M/F]: "))[0]
    if idade > 18:
        contador_maioridade += 1
    if sexo in "Ff": 
        if idade < 20:
            contador_feminino_menor += 1
    else:
        contador_masculino += 1    
    continuar = " "
    while continuar not in "SsNn":
        continuar = str(input("Quer continuar? [S/N]: ")).strip()[0]
    if continuar in "Nn":
        break
print(f"PROCESSO DE CADASTRO ENCERRADO. ")
print(f"{contador_maioridade} pessoas cadastradas tem mais de 18 anos;")
print(f"{contador_masculino} Homens foram cadastrados;")
print(f"{contador_feminino_menor} Mulheres tem menos de 20 anos")
