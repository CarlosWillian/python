valores = []

for c in range(0, 5):
    v = int(input('Digite um valor: '))
    if c == 0 or v > valores[-1]:
        valores.append(v)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if v <= valores[pos]:
                valores.insert(pos, v)
                break
            pos += 1
        print(f'Adicionado na posição {pos} da lista...')
print('-='*18)
valores.sort()
print(f'Os valores digitados em ordem foram {valores}')