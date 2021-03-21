matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = t = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o número para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]
        if matriz[l][2]:
            t += matriz[l][c]
        if l == 1:
            mai = matriz[l][c]
            if matriz[l][c] > mai:
                mai = matriz[l][c]
print('-=' * 24)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[  {matriz[l][c]:^5}  ]', end='')
    print()
print('-=' * 24)
print(f'A soma de todos os valores pares é {s}')
print(f'A soma dos valores da terceira coluna é {t}')
print(f'O maior valor da linha 2 é o {mai}')

