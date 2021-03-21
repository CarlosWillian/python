pessoas = {'nomes': 'Carlos', 'sexo': 'M', 'idade': 25}
del pessoas['idade']
pessoas['nomes'] = 'Lucas'
pessoas['peso'] = 70
for k, v in pessoas.items():
    print(f'{k} = {v}')
