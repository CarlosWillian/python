temp = list()
princ = list()
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sn == 'N':
        break
print('-=' * 24)
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai} Kg, ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {men} Kg, ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
