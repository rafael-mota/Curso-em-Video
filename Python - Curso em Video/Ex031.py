num = int(input(f'Digite a distância que irá percorrer em kilometros: '))
if num <= 200:
    print(f'Sua distância percorrida será de {num}KM \nO valor a pagar pela viagem é de: R${num*float(0.50):.2f}')
else:
    print(f'Sua distância percorrida será de {num}KM \nO valor a pagar pela viagem é de: R${num*float(0.45):.2f}')