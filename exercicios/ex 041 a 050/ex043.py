print('Cálculo do IMC')

p = float(input('Digite seu peso em quilos: '))
a = float(input('Digite sua altura em metros: '))

imc = p / a**2

print('Seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('VOCÊ ESTÁ NO PESO IDEAL!')
elif 25 <= imc < 30:
    print('VOCÊ ESTÁ COM SOBREPESO!')
elif 30 <= imc < 40:
    print('VOCÊ ESTÁ COM OBESIDADE!')
else:
    print('VOCÊ ESTÁ COM OBESIDADE MÓRBIDA')


