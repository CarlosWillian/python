ano = int(input('Digite seu ano de nascimento: '))

i = 2021 - ano

if i <= 9:
    print('Sua categoria é MIRIM!')
elif 9 < i <= 14:
    print('Sua categoria é INFANTIL!')
elif 14 < i <= 19:
    print('Sua categoria é JUNIOR!')
elif i == 20:
    print('Sua categoria é SÊNIOR!')
elif i > 20:
    print('Sua categoria é MASTER!')
