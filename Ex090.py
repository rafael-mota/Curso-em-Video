#Cadastro simples de alunos com media e situação
alunos = dict()
alunos["aluno"] = str(input("Nome: ")).strip().capitalize()
alunos["media"] = float(input(f"Média de {alunos['aluno']}: "))
print(f"O nome é igual a {alunos['aluno']}")
print(f"Média é igual a {alunos['media']}")
if alunos['media'] >= 7:
    alunos["situação"] = "APROVADO"
elif  5 <= alunos['media'] < 7:
    alunos["situação"] = "RECUPERAÇÃO"
else:
    alunos["situação"] = "REPROVADO"
print(f"A Situação é igual a {alunos['situação']}.")