def contador(i, f, p):
    """
    => Função para contagem
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = 1
    while c <= f:
        print(f"{c}", end=' ')
        c += p
    print("FIM!")

contador(0, 220, 2)

help(contador)