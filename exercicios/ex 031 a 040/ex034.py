print('Aumento de salário')
n = float(input('Digite o seu salário atual: '))

if n > 1250:
    print('Seu novo salário com o reajuste é de R$ {}'.format(n*1.1))
else:
    print('Seu novo salário com o reajuste é R$ {}'.format(n*1.15))
