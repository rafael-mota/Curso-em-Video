#Cadastro de pessoas utilizando listas e dicionários
pessoas = []
mulheres = []
soma_idade = 0

while True:
    pessoa = {}
    pessoa['nome'] = str(input("NOME: ")).strip().capitalize()
    pessoa['sexo'] = str(input("SEXO [M/F]: ")).strip().upper()
    pessoa['idade'] = int(input("IDADE: "))
    soma_idade += pessoa['idade']
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa.copy())
    pessoas.append(pessoa.copy())

    continuar = " "
    while continuar not in "SsNn":
        continuar = str(input("Deseja continuar? [S/N] >>> "))
    if continuar in "Nn":
        break
print("-=-"*18)

media_idade = soma_idade / len(pessoas)

print(f"- Ao total, {len(pessoas)} foram cadastradas no grupo.")
print(f"- A média de idade do grupo é de {media_idade} anos.")
print(f"- As mulheres cadastradas foram: ", end=" ")
for m in mulheres:
    print(m['nome'], end=" ")
print()
print(f"- Lista de pessoas que estão acima da média de idade são: ")
for i in pessoas:
    if i['idade'] > media_idade:
        print()
        print(i)
print("<<< ENCERRADO >>>")