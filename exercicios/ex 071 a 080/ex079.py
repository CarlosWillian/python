valores = []

while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sn == 'N':
        break
print('-='*36)
valores.sort()
print(f'Você digitou os valores {valores}')

