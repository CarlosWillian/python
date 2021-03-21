def contador(*num):
    for v in num:
        print(f'{v}', end=' ')
    print('fim')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)