n = s = tot = 0
while True:
    n = int(input('Digite um número (999 pra parar): '))
    if n == 999:
        break
    s += n
    tot += 1
print(f'A soma dos {tot} números foi {s}!')

