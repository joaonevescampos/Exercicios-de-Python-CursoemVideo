ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['média'] = float(input('Média: '))
print(f'Nome = {ficha["nome"]} ')
print(f'Média = {ficha["média"]}')
if ficha['média'] >= 5:
    print('Situação = APROVADO.')
else:
    print('Situação = REPROVADO.')