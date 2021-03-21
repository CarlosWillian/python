times = ('Flamengo', 'Internacional', 'Atlético Mineiro', 'São Paulo',
         'Fluminense', 'Palmeiras', 'Grêmio', 'Santos', 'Corinthians',
         'Ceará', 'Fortaleza', 'Red Bull', 'Atlético Paranaense', 'Sport',
         'Bahia', 'Chapecoense', 'Vasco', 'Goais', 'Coritiba', 'Botafogo')
print('=' * 24)
print('5 Primeiros colocados:')

for c in range(1, 6):
    print(f'{c}° - {times[c - 1]}')
print('=' * 24)

print('4 últimos colocados:')

for c in range(17, 21):
    print(f'{c}° - {times[c - 1]}')
print('=' * 24)

print('Times em ordem alfabética:')
print(sorted(times))
print('=' * 24)

print(f'O Chapecoese está na {times.index("Chapecoense") + 1}ª posição')



