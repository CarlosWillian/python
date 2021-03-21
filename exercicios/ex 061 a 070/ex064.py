n = 1
s = 0
tot = 0
while n != 999:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    s += n
    tot += 1
print('Você digitou {} números e o somatório ficou de {}'.format(tot - 1, s - 999))



