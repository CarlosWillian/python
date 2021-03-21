from time import sleep
jogadores = []

while True:
    print('-' * 40)
    jogador = {}

    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    for c in range(1, partidas + 1):
        jogador['gols'].append(int(input(f'Quantos gols na {c}ª partida: ')))
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador)
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while sn not in 'SN':
        print('ERRO!, Por favor, digite apenas S ou N.')
        sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sn in 'N':
        break

print(jogadores)
print('-=' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
print('-' * 52)
for k, v in enumerate(jogadores):
    print(f'{k + 1 :>3} ', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('-' * 52)

while True:
    m = int(input('Mostrar dados de qual jogador? Escolha pelo cod (999 para encerrar o programa): '))
    if m == 999:
        break
    if m - 1 >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {m}! Tente Novamente...')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[m - 1]["nome"]}:')
        for p, g in enumerate(jogadores[m - 1]['gols']):
            print(f'   Na {p+1}ª partida fez {g} gols')
    print('-' * 52)


print('FINALIZANDO...')
sleep(2)
print('<<< VOLTE SEMPRE >>>')
