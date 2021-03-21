n1 = float(input('Digite a nota da P1: '))
n2 = float(input('Digite a nora da P2: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m < 6:
    print('Você está reprovado, estude para a V1 desde já!')
else:
    print('Você está aprovado, parabéns pelo desempenho!')

#print('Parabéns' if m >= 6 else 'Estude mais')
