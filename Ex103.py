#Ficha jogador
def ficha(jogador, gols):
    if jogador == "":
        jogador = "<desconhecido>"

    if gols != type(int) or gols == "":
        gols = 0

    return f"O jogador {jogador} fez {gols} gols(s) no campeonato."

nome_jogador = str(input("Nome do jogador: "))
numero_gols = input("Número de gols: ")

print(ficha(nome_jogador, numero_gols))
