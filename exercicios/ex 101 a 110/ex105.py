def notas(*n, sit=False):
    """
    -> Serve para mostrar o desempenho do aluno e a situação de sua média.
    :param n: são as notas do aluno.
    :param sit: é a situação da média deste aluno.
    :return: a ficha do aluno com quantidade de notas, a maior nota, a menor nota, sua média e situação da média.
    Progrma criado por C.W.
    """
    aluno = {}
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['média'] = sum(n) / len(n)
    if sit:
        if aluno['média'] >= 8:
            aluno['situação'] = 'ÓTIMA'
        elif 6 <= aluno['média'] < 8:
            aluno['situação'] = 'BOA'
        else:
            aluno['situação'] = 'RUIM'
    return aluno


#Programa principal
resp = notas(3.5, 2, 7, 6.5, 4, sit=True)
print(resp)
print()
help(notas)
