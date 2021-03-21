frase = 'Curso em vídeo Python'
print('Conte quantas letras -o- possuem na frase: ', frase.count('o'))
print('Fatie a 4 letra: ', frase[3])
print('Fatie do caracter 9 até o final pulando de dois em dois: ', frase[9::2]) #ou frase[9:21:2]
print('Quantos caracteres possuí na frase? ', len(frase))
print('Quantas letras o possuem do 0 até o 13? ', frase.count('o',0,13))
print('Localize onde começa o trecho deo: ', frase.find('deo'))
print('Existe a palavra Curso na frase? ', 'Curso' in frase)
print('Substitua Python por Android: ', frase.replace('Python','Android'))
print('Transforme tudo em maiúsculo: ', frase.upper())
print('Transforme tudo em maiúsculo e depois contes as letras O: ', frase.upper().count('O'))
print('Transforme tudo em minúsculo: ', frase.lower())
print('Deixe só a primeira letra em maiúsculo: ', frase.capitalize())
print('Deixe só as inicias de cada palavra em maiúsculo: ', frase.title())

frase = '   Aprenda Python  '
print('Remova todos os espaços desnecessários da frase: ', frase.strip())
print('Remova só os espaços desnecessários do lado direito: ', frase.rstrip())
print('Remova só os espaços desnecessário do lado esquerdo: ', frase.lstrip())

frase = 'Curso em vídeo Python'
print('Divida a frase onde se refaça os índices: ', frase.split())
dividido = frase.split()
print('Junte com - os elementos de frase: ', '-'.join(dividido))







