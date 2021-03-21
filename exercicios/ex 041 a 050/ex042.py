print('Existência de um triângulo e Classificação')

cores = {'limpa': '\033[m',
         'verde': '\033[1;42m',
         'vermelho': '\033[1;41m'}

n1 = float(input('Comprimento da reta 1: '))
n2 = float(input('Comprimento da reta 2: '))
n3 = float(input('Comprimento da reta 3: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('As três retas {}PODEM{} formar um triângulo!'.format(cores['verde'], cores['limpa']))
    if n1 == n2 == n3:
        print('Este triangulo é Equilátero!')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Este triangulo é Isóceles')
    else:
        print('Este triangulo é Escaleno!')
else:
    print('As três retas {}NÃO PODEM{} formar um triângulo!'.format(cores['vermelho'], cores['limpa']))




