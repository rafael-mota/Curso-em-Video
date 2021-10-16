#Programa de verificação de categoria por idade
from datetime import date

print('>>> VERIFIQUE SUA CATEGORIA DE NATAÇÃO <<<')
nasc = int(input('Digite o seu ano de nascimento: '))
datual = date.today()
ano = datual.year - nasc

if ano <= 9:
    print(f'Você tem {ano} anos. \nSua categoria é MIRIM')
elif ano <= 14:
    print(f'Você tem {ano} anos. \nSua categoria é INFANTIL')
elif ano <= 19:
    print(f'Você tem {ano} anos. \nSua categoria é JUNIOR')
elif ano <= 25:
    print(f'Você tem {ano} anos. \nSua categoria é SÊNIOR')
else:
    print(f'Você tem mais de 20 anos. \nSua categoria é MASTER')
