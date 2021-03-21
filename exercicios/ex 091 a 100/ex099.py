from time import sleep
def lin():
    print('-=' * 40)


def m(* num):
    lin()
    cont = 0
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v} ', end='')
        sleep(0.7)
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    if num != ():
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print(f'Não tem valor que possa ser considerado o maior.')


m(2, 9, 4, 5, 7, 1)
m(4, 7, 0)
m(1, 2)
m(6)
m(0)
m()
