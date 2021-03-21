r = 'S'
tot = 0
s = 0
maior = 0
menor = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? (S/N) ')).upper()
    tot += 1
    s += n
    if tot == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print('Você digitou {} números e a média foi {}'.format(tot, s/tot))
print('O maior número foi {} e o menor número foi {}'. format(maior, menor))

