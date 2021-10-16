#Aluguel de carros
dias = float(input('Por quantos dias você utilizou o carro? '))
km = float(input('Quantos KM rodados? '))
pdias = dias * 60
kmrod = km * 0.15
print(f'O custo do aluguel do veiculo foi de R${pdias + kmrod:.2f}')