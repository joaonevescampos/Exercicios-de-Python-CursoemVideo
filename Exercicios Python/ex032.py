ano = int(input('Qual ano? '))
resto = ano % 4
if resto == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))