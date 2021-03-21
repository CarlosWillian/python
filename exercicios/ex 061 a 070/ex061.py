print('Crie sua P.A. de 10 termos')

n1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão: '))
termo = n1
c = 1
print('A P.A. é (', end='')
while c <= 10:
    print('{}'.format(termo), end='')
    print(', ' if c < 10 else '', end='')
    termo += r
    c += 1
print(')')

