from math import floor
print('=' * 36)
print('{:^36}'.format('BANCO CEV'))
print('=' * 36)

n = int(input('Qual valor você quer sacar? R$ '))
c = floor(n / 50)
c1 = n % 50
v = floor(c1 / 20)
v1 = c1 % 20
d = floor(v1 / 10)
u = v1 % 10
print(f'Total de {c:.0f} cédulas de R$ 50')
print(f'Total de {v:.0f} cédulas de R$ 20')
print(f'Total de {d:.0f} cédulas de R$ 10')
print(f'Total de {u:.0f} cédulas de R$ 1')
print('=' * 36)
print('Volte sempre ao BANCO CEV, tenha um bom dia')
