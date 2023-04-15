#1. Usando lista:
expressao = str(input('Digite uma expressão: '))
pe = []
pd = []
if '(' in expressao:
    ce = expressao.count('(')
    for c in range(0, ce):
        pe.append('(')
if ')' in expressao:
    cd = expressao.count(')')
    for c in range(0, cd):
        pd.append(')')
if len(pe) == len(pd):
    print('\033[32mExpressão válida!')
else:
    print('\033[31mExpressão inválida!')

#2. Sem usar lista:
'''expressao = str(input('Digite uma expressão: '))
pe = expressao.count('(')
pd = expressao.count(')')
if pe == pd:
    print('\033[32mExpressão válida!')
else:
    print('\033[31mExpressão inválida!')'''


