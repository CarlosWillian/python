print('É número primo?')

tot = 0
n = int(input('Digite um número: '))

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi dividido {} vezes'.format(n, tot))
if tot == 2:
    print('O número é \033[33mPRIMO\033[m')
else:
    print('O número \033[31mNÃO É PRIMO\033[m')


