n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
seq = (n1, n2, n3, n4)

print(f'Você digitou os valores {seq}')
print(f'O valor 9 apareceu {seq.count(9)} vezes')

if 3 not in seq:
    print('O valor 3 não apareceu nenhuma vez')
else:
    print(f'O valor 3 apareceu na {seq.index(3) + 1}ª posição')

print('Os valores pares digitados foram: ', end='')
for n in seq:
    if n % 2 == 0:
        print(n, end=' ')





