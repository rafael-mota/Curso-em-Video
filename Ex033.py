num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite o último número: '))
nums = sorted([num1, num2, num3])
print(f'O menor número é: {nums[0]} \nE o maior número é: {nums[2]}')

#Guanabara Code
menor = num1
if num2 < num1 and num2 < num3:
    menor =  num2
if num3 < num1 and num3 < num2:
    menor = num3

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O menor número é {menor} \nE o maior número é: {maior}')



