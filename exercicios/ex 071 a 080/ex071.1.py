print('=' * 36)
print('{:^36}'.format('BANCO CEV'))
print('=' * 36)

n = int(input('Qual valor você quer sacar? R$ '))
total = n
c = 50
totc = 0
while True:
    if total >= c:
        total -= c
        totc += 1
    else:
        print(f'Total de {totc} de R$ {c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        totc = 0
        if total == 0:
            break
