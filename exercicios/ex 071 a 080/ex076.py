listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2,
            'Compasso', 4.2, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*39)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-'*39)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>6.2f}')
print('-'*39)


