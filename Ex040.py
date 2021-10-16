#Calculo de média simples
print('>>> CÁLCULO DE MÉDIA SIMPLES <<<')
mat = float(input('Insira sua nota de MATEMÁTICA: '))
port = float(input('Insira sua nota de PORTUGUÊS: '))
med = (mat + port) / 2
if med < 5:
    print(f'Sua média é {med} e você foi REPROVADO.')
elif med >= 5 and med <= 6.9:
    print(f'Sua média é {med} e você está de RECUPERAÇÃO.')
else:
    print(f'PARABÉNS! Sua média é {med} e você foi APROVADO.')