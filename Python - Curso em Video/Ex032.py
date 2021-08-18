from datetime import date

ano = int(input('Digite um ano para saber se ele é bissexto: '))
if ano % 400 == 0:
    print(f'O ano {ano} é um ano bissexto!')
elif ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano {ano} é um ano bissexto!')
else:
    print(f'O ano {ano} NÃO é um ano bissexto!')

#Guanabara Code
if ano == 0:
    ano == date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')