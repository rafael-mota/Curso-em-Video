#Mini game par ou impar
from random import randint

vitorias = 0

while True:
    num = int(input("Digite um valor >>> "))
    par_ou_impar = " "
    while par_ou_impar not in "PpIi":
        par_ou_impar = str(input("PAR OU ÍMPAR? [P/I] >>> ")).strip()[0]
    cpu_num = randint(0, 100)
    total = cpu_num + num
    condicao = " "
    if total % 2 == 0:
        condicao = "PAR"
        if par_ou_impar in "Pp":
            vitorias += 1
            print(f"Você escolheu {num} e a cpu {cpu_num}. O total foi de {total} e deu {condicao}! \nVOCÊ VENCEU!")
        else:
            break
    elif total % 2 != 0:
        condicao = "ÍMPAR"
        if par_ou_impar in "Ii":
            vitorias += 1
            print(f"Você escolheu {num} e a cpu {cpu_num}. O total foi de {total} e deu {condicao}! \nVOCÊ VENCEU!")
        else:
            break
print(f"Você escolheu {num} e a cpu {cpu_num}. \nO total foi de {total} e deu {condicao}!")
print(f"VOCÊ PERDEU! \nNUMERO TOTAL DE VITORIAS: {vitorias} \nJOGO FINALIZADO.")
