#SIMULADOR DE VALOR A SER PAGO POR PRODUTO
print(f'{"SIMULADOR DE LOJA":=^10}')
preco = float(input("Insira o valor do produto: R$"))
conpag = int(input('''Insira a condição de pagamento: 
1 - À VISTA DINHEIRO ou PIX: 10% de desconto. 
2 - À VISTA NO CARTÃO: 5% de desconto. 
3 - EM ATÉ 2X NO CARTÃO: Valor normal. 
4 - 3X OU MAIS PARCELAS: 20% de juros. 
>>> '''))
if conpag == 1:
    print(f'Valor do produto: R${preco} \nValor com desconto à vista DINHEIRO ou PIX: R${preco - (preco * 0.10):.2f}')
elif conpag == 2:
    print(f'Valor do produto: R${preco} \nValor com desconto à vista CARTÃO: R${preco - (preco * 0.05):.2f}')
elif conpag == 3:
    print(f'Valor do produto: R${preco} \nValor PARCELADO 2X: R${preco:.2f}')
elif conpag == 4:
    vezes = int(input("Em quantas parcelas? "))
    parcela = ((preco + (preco * 0.20)) / vezes)
    print(f'''Valor do produto: R${preco} \nParcelas: {vezes} x R${parcela:.2f} \nVALOR TOTAL PARCELADO COM JUROS DE 20%: R${preco + (preco * 0.20):.2f}''')
else:
    print('Por favor, retome o processo e insira um valor entre 1 e 4.')







print("OBRIGADO PELA PREFERÊNCIA! VOLTE SEMPRE.")