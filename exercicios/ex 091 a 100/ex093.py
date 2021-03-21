jogador = {}

jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
#s = 0
for c in range(1, partidas + 1):
    g = int(input(f'Quantos gols na {c}ª partida: '))
    jogador['gols'].append(g)
    #s += g
#jogador['total'] = s
jogador['total'] = sum(jogador['gols'])
print('-=' * 40)
print(jogador)
print('-=' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 40)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for pos, l in enumerate(jogador['gols']):
    print(f'    => Na {pos + 1}ª partida, fez {l} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
