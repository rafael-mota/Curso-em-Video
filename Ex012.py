#Cupom de desconto 5%
preco = float(input('Digite o valor do produto: R$'))
print(f'O valor do produto é R${preco}\nCom o cupom de 5% aplicado o valor final é R${preco - ((preco * 5) / 100):.2f}')