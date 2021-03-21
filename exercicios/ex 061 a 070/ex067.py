n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*36)
    if n > 0:
        for c in range(0, 10):
            print(f'{n} x {c} = {n*c}')
    print('-'*36)
    if n < 0:
        break
print('O programa de tabuada ENCERROU, volte sempre!')




