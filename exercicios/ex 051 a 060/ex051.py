print('Crie sua P.A. de 10 termos')

n1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão: '))

print('A P.A. é (', end='')
for c in range(n1, r*10, r):
    print('{}'.format(c), end='')
    print(', ' if c < r*9 else '', end='')
print(')')







