def lin(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))


lin('Controle de Terrenos')


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m².')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
