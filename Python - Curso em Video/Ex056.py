#Analisador completo
print(">>> Analisador completo <<<")

idade = 0
nome_homem_mais_velho = ""
idade_homem_mais_velho = 0
contador_fem_menor_idade = 0

for i in range(4):
    print(f"{i + 1}ª PESSOA")
    input_nome = str(input("Nome: "))
    input_idade = int(input("Idade: "))
    input_sexo = str(input("Sexo [M ou F]: ").upper().strip())
    idade += input_idade
    if input_sexo == "M":
        if input_idade > idade_homem_mais_velho:
            idade_homem_mais_velho = input_idade
            nome_homem_mais_velho = input_nome
    elif input_sexo == "F":
        if input_idade < 20:
            contador_fem_menor_idade += 1
    else:
        print("Valor inválido, retome o processo!")
        breakb

print(f"A média de idade do grupo é de {idade / 4} anos")
print(f"O homem mais velho tem {idade_homem_mais_velho} anos e se chama {nome_homem_mais_velho}")
print(f"Ao todo são {contador_fem_menor_idade} mulheres com menos de 20 anos")
