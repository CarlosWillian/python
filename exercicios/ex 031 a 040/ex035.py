print('Existência de um triângulo')

cores = {'limpa': '\033[m',
         'verde': '\033[1;42m',
         'vermelho': '\033[1;41m'}

n1 = float(input('Comprimento da reta 1: '))
n2 = float(input('Comprimento da reta 2: '))
n3 = float(input('Comprimento da reta 3: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('As três retas {}PODEM{} formar um triângulo!'.format(cores['verde'], cores['limpa']))
else:
    print('As três retas {}NÃO PODEM{} formar um triângulo!'.format(cores['vermelho'], cores['limpa']))



