#Analise de grupo de jogadores com dicionários
jogadores = list()

while True:
    print('---'*18)
    jogador = dict()
    jogador['nome'] = str(input("Nome do Jogador: ")).strip().capitalize()
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    jogador['gols'] = []
    for p in range(partidas):
        jogador['gols'].append(input(f"Quantos gols na partida {p}? "))
    jogadores.append(jogador.copy())
    continuar = " "
    while continuar not in "SsNn":
        continuar = str(input("Deseja continuar? [S/N] >>> "))
    if continuar in "Nn":
        break

print("-=-"*18)
print(f"{'cod'}  {'nome'}             {'gols'}                     {'total'}")
print('---'*18)

for n, j in enumerate(jogadores):
    print(f"{n}   {j['nome']:<5}  {j['gols']:<10}")

while True:
    num = int(input("Mostrar dados de qual jogador? "))
    if num == 999:
        break
    elif num in range(len(jogadores)):
        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[num]['nome']}")
        for jogo, gol in enumerate(jogadores[num]['gols']):
            print(f"No jogo {jogo} fez {gol} gols")
        print('---' * 18)
    else:
        print(f"ERRO! Não existe jogador com o código {num}! Tente novamente.")
print("<<< VOLTE SEMPRE >>>")
