#Jogo de dados com dicionários
from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
ranking = list()
print("<<< VALORES SORTEADOS >>")
for i in range(1, 5):
    jogadores[f'Jogador{i}'] = randint(1, 6)
    sleep(1)
    print(f"Jogador{i} tirou {jogadores[f'Jogador{i}']} no dado.")
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
sleep(1)
print(f"== RANKING DOS JOGADORES ==")
for n, j in enumerate(ranking):
    print(f"{n + 1}º LUGAR: {j[0]} com {j[1]}")
    sleep(1)
