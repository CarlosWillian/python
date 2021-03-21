def leiaDinheiro(msg):
    ok = False
    while not ok:
        d = str(input(msg)).replace(',', '.').strip()
        if d.isalpha() or d == '':
            print(f'\033[31mERRO! \"{d}\" é um preço inválido!\033[m')
        else:
            ok = True
            return float(d)

