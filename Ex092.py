#Registro e análise de dados de colaborador
import datetime
while True:
    colaborador = {}
    colaborador['nome'] = str(input("NOME: ")).strip().capitalize()
    idade = (int(input("Ano de nascimento: ")))
    colaborador['idade'] = ((datetime.datetime.today().year) - idade)
    colaborador['CTPS'] = int(input("Número da carteira de trabalho: "))
    if colaborador['CTPS'] == 0:
        break
    colaborador['contratacao'] = int(input("Ano de contratação: "))
    colaborador['salario'] = float(input('Salário: R$'))
    colaborador['aposentadoria'] = (colaborador['contratacao'] + 35)
    break
print(f"O nome do colaborador é {colaborador['nome']}.")
print(f"{colaborador['nome']} tem {colaborador['idade']} anos de idade.")
print(f"O número da CTPS é {colaborador['CTPS']}.")
if colaborador['CTPS'] > 0:
    print(f"Contratação foi no ano de {colaborador['contratacao']}.")
    print(f"O salário de {colaborador['nome']} é de R${colaborador['salario']:.2f}.")
    print(f"A aposentadoria de {colaborador['nome']} será no ano de {colaborador['aposentadoria']} e terá {colaborador['aposentadoria'] - idade} anos.")
