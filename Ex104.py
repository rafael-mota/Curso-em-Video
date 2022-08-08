# Função de leitura estrita a números inteiros.

def leiaInt(frase):
    num = input(frase)
    realNum = 0
    while True:
        if num.isnumeric():
            realNum = int(num)
            return realNum
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
            num = input(frase)


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
