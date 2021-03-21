def aumentar(p=0, taxa=0, formato=False):
    res = p * (taxa / 100 + 1)
    return res if formato is False else moeda(res)


def diminuir(p=0, taxa=0, formato=False):
    res = p * (1 - taxa / 100)
    return res if formato is False else moeda(res)


def dobro(p=0, formato=False):
    res = p * 2
    return res if formato is False else moeda(res)


def metade(p=0, formato=False):
    res = p / 2
    return res if formato is False else moeda(res)


def moeda(p=0, moeda='R$'):
        return f'{moeda}{p:.2f}'.replace('.', ',')


def resumo(p=0, aum=0, red=0):
    print('-' * 40)
    print('{:^40}'.format('RESUMO DO VALOR'))
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{aum}% de aumento: \t{aumentar(p, aum, True)}')
    print(f'{red}% de redução: \t{diminuir(p, red, True)}')
    print('-' * 40)
