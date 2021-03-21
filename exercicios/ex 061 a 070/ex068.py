import random
print('-='*12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*12)
tot = 0
while True:
    n = int(input('Escolha seu número: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Você quer par ou ímpar, [P/I]: ')).upper().strip()[0]
    print('-'*24)
    r = random.randint(1, 10)
    t = n + r
    if t % 2 == 0:
        x = 'PAR'
    else:
        x = 'ÍMPAR'
    print(f'Você jogou {n} e o computador {r}. \nTotal de {t} DEU {x}')
    print('-' * 24)
    if (pi == 'P' and x == 'PAR') or (pi == 'I' and x == 'ÍMPAR'):
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        print('-' * 24)
        tot += 1
    else:
        print('VOCÊ PERDEU')
        break
print(f'GAME OVER. Você venceu {tot} vezes \nTente novamente')

