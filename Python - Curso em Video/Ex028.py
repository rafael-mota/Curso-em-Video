from random import choice
from time import sleep

print('>>> ROBÔ RANDOM NUMBER <<< \nTente adivinhar o número gerado pelo computador ;)')
numpc = int(choice(range(6)))
numus = int(input('Digite um número de 0 á 5: '))
print('Processando...')
sleep(3)
if numus == numpc:
    print(f'O número escolhido pelo Robô foi: {numpc} \nO seu foi: {numus} \nParabéns, você ganhou!')
else:
    print(f'O número escolhido pelo robô foi: {numpc} \nO seu foi: {numus} \nVocê perdeu!')
print('FIM DE OPERAÇÃO DO ROBÔ')

#Guanabara Code
from random import randint
computador = randint(0,5)
print('-=-'*16)
print('Guessing the number from 0 to 5. Try to guess...')
print('-=-'*16)
jogador = int(input('Digite o número desejado: '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! VOCÊ VENCEU!')
else:
    print('VOCÊ PERDEU!')