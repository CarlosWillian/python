from time import sleep
def lin():
    print('-=' * 30)


def contagem(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if f > i:
        if p != 0:
            for c in range(i, f + p, p):
                print(c, end=' ')
                sleep(0.5)
            print('FIM!')
        if p == 0:
            for c in range(i, f + 1, 1):
                print(c, end=' ')
                sleep(0.5)
            print('FIM!')
    else:
        if p > 0:
            for c in range(i, f - p, -p):
                print(c, end=' ')
                sleep(0.5)
            print('FIM!')
        elif p < 0:
            for c in range(i, f + p, p):
                print(c, end=' ')
                sleep(0.5)
            print('FIM!')
        else:
            for c in range(i, f - 1, -1):
                print(c, end=' ')
                sleep(0.5)
            print('FIM!')



lin()
contagem(1, 10, 1)
lin()
contagem(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('{:<8} '.format('Início:')))
fim = int(input('{:<8} '.format('Fim:')))
passo = int(input('{:<8} '.format('Passo:')))
lin()
contagem(ini, fim, passo)
