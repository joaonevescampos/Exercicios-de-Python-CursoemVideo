def voto(nasc):
    """
    Analisa se com idade 'i', seu voto é obrigatório, opcional ou proibido.
    :param i: idade
    :return: Situação de voto: obrigatório, opcional ou proibido.
    """
    from datetime import date
    anoatual = date.today().year
    i = anoatual - nasc
    if i < 18:
        return f'Com {i} anos, você não pode votar ainda!'
    if 18 <= i < 60:
        return f'Com {i} anos, o voto é OBRIGATÓRIO!'
    if i >= 60:
        return f'Com {i} anos, o voto é opcional! '


nasc = int(input('Em qual ano nasceu? '))
print(voto(nasc))
help(voto)
