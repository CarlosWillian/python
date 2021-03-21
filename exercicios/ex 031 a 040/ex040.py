print('Resultado Semestral do aluno')

cores = {'limpa': '\033[m',
         'verde': '\033[1;42m',
         'vermelho': '\033[1;41m',
         'amarela': '\033[1;43m'}

n1 = float(input('Digite sua nota da P1: '))
n2 = float(input('Digite sua nota da P2: '))

m = (n1 + n2)/2

if m < 5:
    print('Sua média é {}, {}REPROVADO{}'.format(m, cores['vermelho'], cores['limpa']))
elif 5 <= m <= 6.9:
    print('Sua média é {}, {}RECUPERAÇÂO{}'.format(m, cores['amarela'], cores['limpa']))
else:
    print('Sua média é {}, {}PARABÉNS, VOCÊ ESTÁ APROVADO{}'.format(m, cores['verde'], cores['limpa']))
