#Analise de dados com tupla
num1 = int(input('Insira um número [1] >>> '))
num2 = int(input('Insira um número [2] >>> '))
num3 = int(input('Insira um número [3] >>> '))
num4 = int(input('Insira um número [4] >>> '))
numtupla = (num1, num2, num3, num4)

print(f"Você digitou os números {numtupla}.")
print(f"O valor 9 apareceu {numtupla.count(9)} vezes.")
try:
    print(f"O valor 3 apareceu na {numtupla.index(3) + 1}ª posição.")
except:
    print(f"O valor 3 não foi digitado em nenhuma posição!")
print(f"Os valores pares digitados foram: ", end="")    
for i in numtupla:
    if i % 2 == 0:
        print(i, end=" ") 
