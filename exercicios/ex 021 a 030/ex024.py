cidade = str(input('Em que cidade você mora: ')).strip().lower()

separar = cidade.split()

print('O primeiro nome da cidade é Santo: {}'.format('santo' in separar[0]))


