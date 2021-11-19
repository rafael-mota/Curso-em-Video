#Análise de dados com dicionários.
jogador = dict()
jogador['nome'] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
jogador['gols'] = []
for i in range(partidas):
    jogador['gols'].append(int(input(f"Quantos gols na partida {i}? ")))
jogador['total'] = sum(jogador['gols'])
print("-=-"*18)
print(jogador)
print("-=-"*18)
print(f"O nome do jogador é {jogador['nome']}.")
print(f"{jogador['nome']} marcou esse número de gols: {jogador['gols']}.")
print(f"Ao total, {jogador['nome']} fez {jogador['total']} gols.")
print("-=-"*18)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
for p in range(partidas):
    print(f"=> Na partida {p}, fez {jogador['gols'][p]} gols.")
print(f"Foi um total de {jogador['total']} gols!")