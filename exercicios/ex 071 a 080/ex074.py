from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {n}')
print(f'O maior valor sorteado foi: {max(n)}')
print(f'O menos valor sorteado foi: {min(n)}')
