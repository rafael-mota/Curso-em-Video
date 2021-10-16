#Calculo IMC

peso = float(input('Insira seu peso (kg): '))
alt = float(input('Insira sua altura (m): '))
imc = peso / (alt * alt)

if imc < 18.5:
    print(f"Seu IMC é de {imc:.2f} - Você está ABAIXO DO PESO")
elif imc >= 18.5 and imc < 25:
    print(f"Seu IMC é de {imc:.2f} - Você está com o PESO IDEAL")
elif imc >= 25 and imc < 30:
    print(f"Seu IMC é de {imc:.2f} - Você está com SOBREPESO")
elif imc >= 30 and imc < 40:
    print(f"Seu IMC é de {imc:.2f} - Você está com OBESIDADE")
else:
    print(f"Seu IMC é de {imc:.2f} - Você está com OBESIDADE MORBIDA")


