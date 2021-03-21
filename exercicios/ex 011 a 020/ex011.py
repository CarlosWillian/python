print('Quantos litros de tinta para pintar minha parede?')
n1 = float(input('Digite a largura em metros da sua parede: '))
n2 = float(input('Digite a altura em metros da sua parede: '))
n3 = n1*n2
print('A área da sua parede é: {}m²'.format(n3))
print('Litros de tinta necessários para pintar sua parede: {}L'.format(n3/2))
