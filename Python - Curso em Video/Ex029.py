car = float(input('Insira a velocidade do carro: '))
if car >= float(80):
    print(f'Você acaba de ser multado! \nA multa vai custar R${float((car - 80) * 7):.2f}')
else:
    print(f'Você está dentro da velocidade.')

