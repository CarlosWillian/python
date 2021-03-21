print('Ex. Formas de Pagamento')

n = float(input('Valor da sua compra: R$ '))

print('Formas de Pagamento:')

print('''1 - À vista no dinheiro ou cheque
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão''')

p= int(input('Escolha uma das formas de pagamento para saber o valor final da sua compra: '))

p1 = n * 0.9
p2 = n * 0.95
p4 = n * 1.2

if p == 1:
    print('Você terá 10% de desconto e o valor final da sua compra será de R$ {}'.format(p1))
elif p == 2:
    print('Você terá 5% de desconto e o valor final da sua compra será de R$ {}'.format(p2))
elif p == 3:
    parcela = n / 2
    print('Você não terá desconto e o valor final da sua compra será de R$ {} com duas parcelas de R$ {}'.format(n, parcela))
elif p == 4:
    parcelas = float(input('Quantas parcelas serão? '))
    par = p4 / parcelas
    print('Você terá 20% de juros e o valor final da sua compra será de R$ {}, {} parcelas de R$ {}'
          .format(p4, parcelas, par))
else:
    print('Opção inválida, tente novamente!')

