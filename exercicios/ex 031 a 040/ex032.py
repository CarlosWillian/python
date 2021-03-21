ano = int(input('Digite um ano qualquer: '))
print('Analisando...')

cores = {'limpa': '\033[m',
         'verde': '\033[4;42m',
         'vermelho': '\033[4;41m'}

#para anos múltiplos de 4
a1 = ano % 4
a2 = ano % 100
a3 = ano % 400
if a1 == 0 and a2 != 0 or a3 == 0:
    print('O ano de {} é {}BISSEXTO!{}'.format(ano, cores['verde'], cores['limpa']))
else:
    print('O ano de {} {}NÃO É BISSEXTO!{}'.format(ano, cores['vermelho'], cores['limpa']))




