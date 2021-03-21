grupo = []
i = 0
while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: ')).upper().strip()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    i += pessoa['idade']
    grupo.append(pessoa)
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while sn not in 'SN':
        print('ERRO!, Por favor, digite apenas S ou N.')
        sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sn in 'N':
        break

print(grupo)
print('-=' * 40)
print(f'- O grupo tem {len(grupo)} pessoas.')
media = i / len(grupo)
print(f'- A média de idade é de {media:5.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for pessoa in grupo:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]}', end=' ')
print()
print('- Lista de pessoas que estão acima da média:')
print()
for pessoa in grupo:
    if pessoa['idade'] > media:
        for k, v in pessoa.items():
            print(f'{k} = {v};', end=' ')


