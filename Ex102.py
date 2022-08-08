#Calculo Fatorial Avançado - Mostra a conta ou não por definição do usuário.
def fatorial(n=1, show="Nn"):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor Fatorial de um número n.
    """
    f = 1
    while n > 0:
        if show in "Ss":
            print(n, end=" ")
            if n > 1:
                print("X", end=" ")
            else:
                print("=", end=" ")
        f *= n
        n -= 1
    return f
num = int(input("Digite um número para calcular seu Fatorial: "))
#Bloco de checagem Sim ou Não para mostrar Fatorial
mostrar = " "
while mostrar not in "SsNn":
    mostrar = str(input("Digite SIM ou NÃO -> Completo? S/N ")).strip()[0]
print(fatorial(num, mostrar))
