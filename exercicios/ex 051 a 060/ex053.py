print('A frese é palíndromo?')

frase = str(input('Escreva uma frase sem pontuação e acentos: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('A frase é PALÍNDROMO')
else:
    print('A frase NÃO É PALÍNDROMO')








