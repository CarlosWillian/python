from datetime import datetime
dados = dict()

dados['nome'] = str(input('Nome: '))
#dados['idade'] = 2021 - int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    #dados['aposentadoria'] = 35 - (2021 - dados['contratação']) + dados['idade']
    dados['aposentadoria'] = dados['idade'] + 35 + dados['contratação'] - datetime.now().year

print('-=' * 40)
print(dados)
for k, v in dados.items():
    print(f'   - {k} tem o valor {v}')
