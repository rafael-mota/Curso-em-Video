# Módulo de manipulação monetária

def metade(valor):
    return valor / 2


def dobro(valor):
    return valor * 2


def aumentar(valor, porcentagem):
    aumentado = (valor * porcentagem) / 100
    return aumentado + valor


def diminuir(valor, porcentagem):
    diminuido = (valor * porcentagem) / 100
    return valor - diminuido
