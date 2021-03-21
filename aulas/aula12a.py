nome = str(input('Digite seu nome: '))
if nome == 'Carlos':
    print('Que nome lindo!')
elif nome == 'Maria' or nome == 'Lucas' or nome == 'João':
    print('Seu nome é muito comum no Brasil!')
elif nome in 'Ana Carla Creuza Luiza':
    print('Que belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))

