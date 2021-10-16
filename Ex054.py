#Grupo de maioridade
from datetime import date
maior = 0
menor = 0
anoatual = date.today().year
for i in range(1, 8):
    nasc = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    if nasc > anoatual:
        print('Retome o processo e insira uma data válida.')
        break
    elif (anoatual - nasc) > 18:
        maior += 1
    else:
        menor += 1
print(f"Ao todo o sistema contabilizou {maior} pessoas maiores de idade e {menor} menores de idade.")