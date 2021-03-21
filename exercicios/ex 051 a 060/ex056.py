print('Nome, Idade e Sexo')
velho = 0
nomevelho = 0
m = 0
totM = 0
tot20 = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    n = str(input('Digite seu nome: ')).strip()
    i = int(input('Sua idade: '))
    s = str(input('Seu sexo (M/F): ')).upper().strip()

    m += i

    if c == 1 and s == 'M':
        velho = i
        nomevelho = n
    if s == 'M' and i > velho:
        velho = i
        nomevelho = n

    if s == 'F':
        totM += 1
    if s == 'F' and i < 20:
        tot20 += 1

print('A média de idade do grupo é {} anos'.format(m/4))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nomevelho))
print('Exitem {} mulheres no grupo e {} delas tem menos de 20 anos'.format(totM, tot20))

