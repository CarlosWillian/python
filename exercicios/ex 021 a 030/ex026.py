frase = str(input('Digite uma frase qualquer: ')).lower().strip()

print('a letra A aparece {} vezes'.format(frase.count('a')))
print('a primeira letra A aparece na {}° posição'.format(frase.find('a')+1))
print('a última letra A aparece na {}° posição'.format(frase.rfind('a')+1))






