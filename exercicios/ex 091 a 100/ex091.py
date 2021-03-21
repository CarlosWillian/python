from time import sleep
from random import randint
from operator import itemgetter

numeros = dict()
print('Valores sorteados:')
print('-' * 20)
for c in range(1, 5):
    numeros[f'jogador{c}'] = randint(1, 6)
    print(f'O jogador{c} tirou {numeros[f"jogador{c}"]}')
    sleep(1)


print('-' * 20)
print('Ranking dos jogadores:')
ranking = sorted(numeros.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
print()
