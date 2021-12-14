#contador com funções
from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = passo - passo * 2

    print("-=" * 20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio < fim:
        while inicio <= fim:
            print(inicio, end=" ")
            inicio += passo
            sleep(0.5)
    elif inicio > fim:
        while inicio >= fim:
            print(inicio, end=" ")
            inicio -= passo
            sleep(0.5)
    print("FIM!")

contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é sua vez de personalizar a contagem!")
contador(int(input("Início: ")), int(input("Fim: ")), int(input("Passo: ")))