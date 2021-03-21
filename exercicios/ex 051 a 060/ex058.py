import random

print('''Olá, sou seu computador!
Acabei de pensar em um número.
Será que você consegue adivinhar?''')

n = random.randint(0, 10)
tot = 0
num = int(input('Escolha um número de 0 a 10: '))
while num != n:
    tot = tot + 1
    if num < n:
        num = int(input('Mais... Escolha outro número: '))
    else:
        num = int(input('Menos... Escolha outro número: '))


print('Você acertou, o número foi {} e você precisou de {} tentativas para acertar!'.format(n, tot + 1))



