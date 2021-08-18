print('>>> Calculo de ajuste salarial 2021 <<<')
sal = float(input('Digite o valor do seu salario: R$'))
if sal > float(1250.00):
    print(f'Seu novo salario com ajuste de 10% será de R${(sal + (sal * 0.10)):.2f}')
else:
    print(f'Seu novo salario com ajuste de 15% será de R${(sal +(sal * 0.15)):.2f}')