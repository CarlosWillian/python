from time import sleep
ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sn == 'N':
        break
print('-=' * 36)
print('{}  {:<12}  {}'.format('N°', 'NOME', 'MÉDIA'))
print('-' * 25)
for pos, c in enumerate(ficha):
    print('{}   {:<12}  {:.1f}'.format(pos + 1, ficha[pos][0], ficha[pos][2]))
print('-' * 25)


while True:
    mostrar = int(input('Mostar notas de qual aluno? Escolha pelo N° dele (digite 999 para interromper): '))
    if mostrar == 999:
        break
    print(f'Notas de {ficha[mostrar - 1][0]} são {ficha[mostrar - 1][1]}')
    print('-' * 25)

print('FINALIZANDO...')
sleep(2)
print('<<< VOLTE SEMPRE >>>')
