print('Conversão de bases numéricas')

n = int(input('Digite um número inteiro que deja converter: '))
print('Escolha a base de conversão: \n1 - Binário \n2 - Octal \n3 - Hexadecimal')

choice = int(input('Digite o número correspondente a sua escolha: '))

if choice == 1:
    print('O número {} convertido para base Binária é {}'.format(n, bin(n)[2:]))
elif choice == 2:
    print('O número {} convertido para base Octal é {}'.format(n, oct(n)[2:]))
elif choice == 3:
    print('O número {} convertido para base Hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, tente novamente!')

