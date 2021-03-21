def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16:
        return f'Com {idade} anos. NÃO VOTA AINDA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('-' * 30)
a = int(input('Em que ano você nasceu? '))
print(voto(a))
