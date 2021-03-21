import emoji
import random
import time

cores = {'limpa': '\033[m',
         'verde': '\033[1;42m',
         'vermelho': '\033[1;41m',
         'amarela': '\033[1;43m'}

print('Jokenpô')

r = emoji.emojize(':punch:', use_aliases=True)
p = emoji.emojize(':hand:', use_aliases=True)
s = emoji.emojize(':v:', use_aliases=True)
lista = (r, p, s)
n = random.choice(lista)

print(emoji.emojize('''Jogue contra o computador!
Escolha a sua arma:
r - :punch:
p - :hand:
s - :v:''', use_aliases=True))

arma = str(input('Qual sua arma? ')).lower()

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')

if arma == 'r':
    print('VOCÊ ------ COMPUTADOR \n {}   ------      {}'.format(r, n))
elif arma == 'p':
    print('VOCÊ ------ COMPUTADOR \n {}   ------      {}'.format(p, n))
elif arma == 's':
    print('VOCÊ ------ COMPUTADOR \n {}   ------      {}'.format(s, n))
else:
    print('Opção inválida, tente novamente!')

if arma == 'r' and n == r:
    print('{}EMPATE{}'.format(cores['amarela'], cores['limpa']))
elif arma == 'r' and n == p:
    print('{}VOCÊ PERDEU{}'.format(cores['vermelho'], cores['limpa']))
elif arma == 'r' and n == s:
    print('{}VOCÊ VENCEU{}'.format(cores['verde'], cores['limpa']))

if arma == 'p' and n == p:
    print('{}EMPATE{}'.format(cores['amarela'], cores['limpa']))
elif arma == 'p' and n == s:
    print('{}VOCÊ PERDEU{}'.format(cores['vermelho'], cores['limpa']))
elif arma == 'p' and n == r:
    print('{}VOCÊ VENCEU{}'.format(cores['verde'], cores['limpa']))

if arma == 's' and n == s:
    print('{}EMPATE{}'.format(cores['amarela'], cores['limpa']))
elif arma == 's' and n == r:
    print('{}VOCÊ PERDEU{}'.format(cores['vermelho'], cores['limpa']))
elif arma == 's' and n == p:
    print('{}VOCÊ VENCEU{}'.format(cores['verde'], cores['limpa']))








