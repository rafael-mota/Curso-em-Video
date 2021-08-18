#Verificação de alistamento
from datetime import date

print('>>> VERIFICAÇÃO DE IDADE PARA ALISTAMENTO MILITAR <<<')
nasc = int(input('Insira seu ano de nascimento: '))
hoje = date.today()
idcalc = hoje.year - nasc
print(f'Você tem {idcalc} anos em {hoje.year}.')
if idcalc < 18:
    print(f'Faltam {18 - idcalc} anos para você se alistar no serviço militar')
elif (hoje.year - nasc) == 18:
    print(f'Você tem {idcalc} anos. \nJá é hora de se alistar no serviço militar!')
else:
    print(f'O período para alistamento foi à {idcalc - 18} anos! \nProcure o posto militar mais próximo e regularize sua situação.')
