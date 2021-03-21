n = int(input('Digite um número inteiro qualquer: '))
resultado = n % 2

cores = {'limpa': '\033[m',
         'amareloroxo': '\033[1;33;100m',
         'brancociano': '\033[1;97;46m'}

print('Analisando...')
if resultado == 1:
    print('O número {} é {}ÍMPAR!{}'.format(n, cores['amareloroxo'], cores['limpa']))
else:
    print('O número {} é {}PAR!{}'.format(n, cores['brancociano'], cores['limpa']))


