print('Fatorial!')

'''n = int(input('Digite um número: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print(f)'''

f = 1
n = int(input('Digite um número: '))
print('Calculando {}! = '.format(n), end='')
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f)









