vel = float(input('Velocidade regstrada do carro em km/h: '))

if vel > 80:
    print('Você foi multado e sua multa é de R$ {}'.format(7*(vel-80)))
else:
    print('Sua velocidade está adequada, continue assim!')

