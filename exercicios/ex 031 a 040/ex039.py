print('Hora de se alistar? Vamos descobrir!')

ano = int(input('Digite o ano que você nasceu: '))

r = 2021 - ano

if r < 18:
    print('Ainda não chegou a hora do seu alistamento, anos que ainda faltam: {}'.format(18-r))
elif r == 18:
    print('Está na hora de você se alistar, fique atento!')
else:
    print('Já passou {} anos da hora de você se alistar, pague a multa!'.format(r-18))
