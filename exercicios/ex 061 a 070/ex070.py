print('-' * 36)
print('{:^36}'.format('LOJA SUPER BARATÃO'))
print('-' * 36)
t = tot = v = 0
barato = 0
nomebarato = ''
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    tot += 1
    if tot == 1:
        barato = preco
        nomebarato = nome
    else:
        if preco < barato:
            barato = preco
            nomebarato = nome
    if preco > 1000:
        v += 1
    t += preco
    sn = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sn == 'N':
        break
print('{:-^36}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${t:.2f}')
print(f'Temos {v} produtos qu custam mais de R$ 1000,00')
print(f'O produto mais barato foi {nomebarato} e custou {barato:.2f}')



