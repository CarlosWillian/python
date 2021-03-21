print('Sequência de Fibonacci')
print('='*24)
t = int(input('Número de termos da sequência: '))
print('='*24)
c = 3
termo1 = 0
termo2 = 1
print('A sequência é ({}, {}, '.format(termo1, termo2), end='')
while c <= t:
    termo3 = termo1 + termo2
    print('{}'.format(termo3), end='')
    print(', ' if c < t else '', end='')
    c += 1
    termo1 = termo2
    termo2 = termo3
print(')')
