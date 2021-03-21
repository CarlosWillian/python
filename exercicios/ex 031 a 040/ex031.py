km = float(input('Qual a distância em km da sua viagem? '))
print('Calculando preço da passagem...')
if km <= 200:
    print('O valor da sua passagem é R$ {:.2f}'.format(km*0.5))
else:
    print('O valor da sua passagem é R$ {:.2f}'.format(km*0.45))
