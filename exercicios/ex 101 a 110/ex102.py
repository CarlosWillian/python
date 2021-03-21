def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número:
    :param n: O número a ser cálculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    Programa criado por C.W.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(f'{c}', end=' x ')
            else:
                print(f'{c} = ', end='')
        f *= c
    return f


#Programa principal
print(fatorial(5, True))
print()
help(fatorial)
