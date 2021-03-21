valores = []

while True:
    v = valores.append(int(input('Digite um valor: ')))
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sn == 'N':
        break
print(f'Você digitou {len(valores)} valores.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte dessa lista e esta na posição {valores.index(5)} da lista!')
else:
    print('O valor 5 não faz parte dessa lista!')
