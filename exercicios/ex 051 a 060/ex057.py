print('Qual seu sexo?')

sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, tente novamente. [M/F] ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
