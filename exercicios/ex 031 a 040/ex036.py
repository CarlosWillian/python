print('Financiamento de imóvél')

cores = {'limpa': '\033[m',
         'verde': '\033[1;42m',
         'vermelho': '\033[1;41m',
         'amarelo': '\033[1;43m'}

casa = float(input('Qual é o valor da casa? R$ '))
sal = float(input('Qual seu salário? R$ '))
anos = float(input('Em quantos anos deseja pagar? '))

m = casa / (12*anos)

print('A prestação mensal para o valor de R${} no imóvel em {} anos é de {}R$ {:.2f}{}'
      .format(casa, anos, cores['amarelo'], m, cores['limpa']))

lim = sal * 0.3

if m > lim:
    print('Infelizmente o valor da prestação ultrapassou 30% do seu salário, {}financiamento negado!{}'
          .format(cores['vermelho'], cores['limpa']))
else:
    print('Seu financiamento foi {}aprovado, parabéns!{}'.format(cores['verde'], cores['limpa']))

