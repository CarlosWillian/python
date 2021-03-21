import random
num = int(input('Escolha um número entre 1 e 5 para participar do sorteio: '))
n = random.randint(1, 5)
print('O número sorteado é {}'.format(n))
if num == n:
    print('PARABÉNS, VOCÊ VENCEU!')
else:
    print('INFELIZMENTE NÃO FOI DESTA VEZ, TENTE NOVAMENTE')

