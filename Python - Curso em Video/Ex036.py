#Programa de aprovação de empréstimo
imovel = float(input('Insira o valor total do imóvel: R$'))
salario = float(input('Insira o valor do seu salário mensal: R$'))
tempo = int(input('Insira o tempo previsto para pagamento em anos: '))
mensalidade = imovel / (tempo * 12)
validacao = salario * 0.30
print(f'Para pagar uma casa de R${imovel:.2f} em {tempo} anos a mensalidade seria de R${mensalidade:.2f}')
if mensalidade <= validacao:
    print(f'Sucesso! Seu empréstimo foi aprovado!')
else:
    print("Devido ao valor da mensalidade ser maior que 30% do seu salário, ficamos impossibilitados de aprovar o empréstimo.")
