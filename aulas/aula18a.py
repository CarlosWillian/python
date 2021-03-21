teste = list()

teste.append('Carlos')
teste.append(25)
print(teste)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 49
galera.append(teste[:])
print(galera)

