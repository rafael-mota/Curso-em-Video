#Analise de varios parametros com funções
from time import sleep


def maior(*num):
    print("-="*23)
    maior = 0
    print("Analisando os valores passados... ")
    for i in num:
        sleep(0.3)
        print(i, end=" ")
        if i > maior:
            maior = i

    sleep(0.5)
    print(f"Foram informados {len(num)} valores ao todo.")
    print(f"O maior valor informado foi {maior}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()