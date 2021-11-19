#Jogo de dados com dicionários
from random import randint
from time import sleep
jogadores = dict()
print("VALORES SORTEADOS:")
for i in range(1, 5):
    jogadores[f'Jogador{i}'] = randint(1, 6)
    sleep(1)
    print(f"Jogador {i} tirou {jogadores[f'Jogador{i}']}")
print(jogadores)