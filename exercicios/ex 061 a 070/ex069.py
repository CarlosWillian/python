i = 0
s = 0
m = 0
while True:
    print('-' * 24)
    print('{:^24}'.format('CADASTRE UMA PESSOA'))
    print('-' * 24)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    if idade > 18:
        i += 1
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        s += 1
    if idade < 20 and sexo == 'F':
        m += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('-' * 24)
    x = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
    while x not in 'SN':
        x = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
    if x == 'N':
        break
print('-' * 24)
print(f'Total de pessoas com mais de 18 anos é {i}')
print(f'Ao todo temos {s} homens cadastrados')
print(f'E temos {m} mulheres com menos de 20 anos')



