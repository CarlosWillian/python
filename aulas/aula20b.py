def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa principal
soma(b=4, a=5)
soma(4, 5)


def sum(* v):
    s = 0
    for n in v:
        s += n
    print(f'Somando os valores {v} temos {s}')


sum(5, 2)
sum(2, 9, 4)
