#Palpites MEGASENA
import time
from random import randint

print(f"{'-'*40}\n          JOGOS DA MEGA SENA  \n{'-'*40}")
num_jogos = int(input("Quantos jogos você quer que eu sorteie? "))
print(f"       >>> SORTEANDO {num_jogos} jogos <<<")
jogos = []
for i in range(num_jogos):
    jogos.append(list())
    for numeros in range(6):
        num = (randint(1, 60))
        if num in jogos[i]:
            num = (randint(1, 60))
        jogos[i].append(num)
    jogos[i].sort()
    time.sleep(1)
    print(f"    JOGO {i+1}: {jogos[i]}")
print(f"\n ♣☻♣☻♣☻♣☻♣ BOA SORTE! ♣☻♣☻♣☻♣☻♣")