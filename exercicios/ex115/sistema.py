from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Lista de Cadastrados', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resp == 1:
        #Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)

    elif resp == 2:
        #Opção de cadastrar nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resp == 3:
        #opção de sair do sistema
        cabecalho('Saindo do Sistema... ATÉ LOGO!')
        break
    else:
        print('\033[31mDigite uma opção válida!\033[m')
    sleep(1)
