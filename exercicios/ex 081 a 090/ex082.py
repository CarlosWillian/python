lista1 = []
lista2 = []  # pares
lista3 = []  # ímpares

while True:
    n = lista1.append(int(input('Digite um número: ')))
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sn == 'N':
        break

for c in lista1:
    if c % 2 == 0:
        lista2.append(c)
    else:
        lista3.append(c)

print('-='*18)
print(f'A lista completa é {lista1}')
print(f'A lista de pares é {lista2}')
print(f'A lista de ímpares é {lista3}')
