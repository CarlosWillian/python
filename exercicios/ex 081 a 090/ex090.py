pessoa = dict()

pessoa['Nome'] = str(input('Nome: '))
pessoa['Média'] = float(input(f'Média de {pessoa["Nome"]}: '))
if pessoa['Média'] < 7:
    pessoa['Situação'] = 'Reprovado'
else:
    pessoa['Situação'] = 'Aprovado'

for k, v in pessoa.items():
    print(f'{k} é igual a {v}')


