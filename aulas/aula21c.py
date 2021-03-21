def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por C.W.
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(c=4, b=2)
somar(8, 4)
somar()
print()
help(somar)
