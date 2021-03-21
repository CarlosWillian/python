from random import randint
from time import sleep
print('-' * 36)
print('{:^36}'.format('JOGOS DA MEGA SENA'))
print('-' * 36)

qnt = int(input('Quantos jogos você quer gerar? '))
print('-' * 3, f'    SORTEANDO {qnt} JOGOS    ', '-=' * 3)
jogos = []
lista = []
tot = 1
while tot <= qnt:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('Boa sorte no seu jogo, divida o prêmio comigo!')

