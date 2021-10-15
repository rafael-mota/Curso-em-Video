#TABUADA VERSÃO WHILE
print(">>> TABUADA CONTINUA <<<")
num = int(input("Quer ver a tabuada de qual número? {DIGITE UM NÚMERO NEGATIVO PARA FINALIZAR} >>> "))
print("=-="*5)
contador = 0
while num > 0:
    while True:
        print(f"{num} x {contador} = {num*contador}")
        contador += 1
        if contador > 10:
            break
    contador = 0
    print("=-="*5)
    num = int(input("Quer ver a tabuada de qual número? {DIGITE UM NÚMERO NEGATIVO PARA FINALIZAR} >>> "))
    print("=-=" * 5)
print("PROCESSO FINALIZADO")