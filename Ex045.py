#JOKENPO
import random
import time

print("DESAFIE A CPU PARA UMA PARTIDA DE JOKENPÔ")
ppt = int(input("SELECIONE PEDRA, PAPEL OU TESOURA: \n'\033[1;37;40m1 - PEDRA\033[m' \n'\033[1;97;40m2 - PAPEL\033[m' \n'\033[1;33;40m3 - TESOURA\033[m' \n>>> "))
cpu = random.randint(1, 3)
print('=-'*11)
print('\033[1;31;40mJO\033[m')
time.sleep(1)
print('\033[1;31;40mKEN\033[m')
time.sleep(1)
print('\033[1;31;40mPO\033[m')
time.sleep(0.3)
print('=-'*11)

if ppt == 1 and cpu == 2:
    print("Você selecionou PEDRA \nA CPU selecionou PAPEL \n>>> VOCÊ PERDEU <<<")
elif ppt == 1 and cpu == 3:
    print("Você selecionou PEDRA \nA CPU selecionou TESOURA \n>>> VOCÊ VENCEU <<<")
elif ppt == 2 and cpu == 1:
    print("Você selecionou PAPEL \nA CPU selecionou PEDRA \n>>> VOCÊ VENCEU <<<")
elif ppt == 2 and cpu == 3:
    print("Você selecionou PAPEL \nA CPU selecionou TESOURA \n>>> VOCÊ PERDEU <<<")
elif ppt == 3 and cpu == 1:
    print("Você selecionou TESOURA \nA CPU selecionou PEDRA \n>>> VOCÊ PERDEU <<<")
elif ppt == 3 and cpu == 2:
    print("Você selecionou TESOURA \nA CPU selecionou PAPEL \n>>> VOCÊ VENCEU <<<")
else:
    print("Você selecionou o mesmo que a CPU  \n>>> EMPATE <<<")