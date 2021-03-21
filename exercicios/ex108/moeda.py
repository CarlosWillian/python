def aumentar(p=0, taxa=0):
    return p * (taxa / 100 + 1)


def diminuir(p=0, taxa=0):
    return p * (1 - taxa / 100)


def dobro(p=0):
    return p * 2


def metade(p=0):
    return p / 2


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')
