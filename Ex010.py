#Conversor de real para dolares
conv = input('Digite o quanto você tem em real: R$')
print(f'Você tem R${conv} em reais \nNa conversão atual você poderá comprar US${float(conv) / float(5.12):.2f} dolares americanos')