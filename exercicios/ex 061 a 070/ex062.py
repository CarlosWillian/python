print('Crie sua P.A. de n termos')

n1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão: '))
total = 0
mais = 10
termo = n1
c = 1
print('A P.A. é (', end='')
while mais != 0:
    total += mais
    while c <= total:
        print('{}'.format(termo), end='')
        print(', ' if c < total else '', end='')
        termo += r
        c += 1
    print('), pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('A P.A. foi finalizada com {} termos!'.format(total))
