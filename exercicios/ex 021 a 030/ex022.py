nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúsculas é: {} '.format(nome.upper()))
print('Seu nome em minúsculas é: ', nome.lower())
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
print('Seu primeiro é {} e ele tem {} letras'.format(separa[0], len(separa[0])))



