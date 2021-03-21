print('Já atingiu a maior idade?')
x = 0
s = 0
for c in range(1, 8):
    ano = int(input('Em que ano nasceu a {}ª pessoa: '.format(c)))
    if ano < 2003:
        s = s + 1
print('Pessoas MAIORES de idade {} \nPessoas MENORES de idade {}'.format(s, 7 - s))




