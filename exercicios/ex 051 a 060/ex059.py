import time
n1 = float(input('Digite o 1° valor: '))
n2 = float(input('Digite o 2° valor: '))

print('''
Escolha uma das opções do menu:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
o = 1
while o != 5:
    o = int(input('Digite a opção escolhida: '))
    if o == 1:
        print('A valor de {} + {} = {}'.format(n1, n2, n1 + n2))
        print(12*'=-')
        time.sleep(1.5)
        print('''Escolha uma das opções do menu:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    if o == 2:
        print('A valor de {} x {} = {}'.format(n1, n2, n1 * n2))
        print(12 * '=-')
        time.sleep(1.5)
        print('''Escolha uma das opções do menu:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    if o == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior que o número {}'.format(n2, n1))
        else:
            print('Os números são iguais!')
        print(12 * '=-')
        time.sleep(1.5)
        print('''Escolha uma das opções do menu:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    if o == 4:
        n1 = float(input('Digite o 1° valor: '))
        n2 = float(input('Digite o 2° valor: '))
        print('''Escolha uma das opções do menu:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')

print('O programa acabou!')
