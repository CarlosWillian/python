from time import sleep


def contagem(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    Função criada por C.W.
    """
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if f >= i:
        for c in range(i, f + p, p):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')


contagem(1, 3, 1)
print()
help(contagem)

