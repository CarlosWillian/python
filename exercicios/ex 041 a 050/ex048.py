import math
print('Soma dos números ímpares múltiplos de 3 no intervalo de 1 a 500')
s = 0
cont = 0
for c in range(1, 500, 2):
    m = c % 3
    if m == 0:
        cont += 1
        s = s + c
print('A soma dos {} números solicitados é {}'.format(cont, s))









