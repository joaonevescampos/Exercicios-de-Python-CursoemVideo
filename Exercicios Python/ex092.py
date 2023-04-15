cadastro = dict()
from datetime import date
cadastro['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
cadastro['idade'] = date.today().year - nascimento
cadastro['ctps'] = int(input('Carteira de trabalho (0 se não tiver): '))

if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: '))
    aposentadoria = cadastro['contratação'] - nascimento + 35
    cadastro['aposentadoria'] = aposentadoria
    print(cadastro)
    print(f'Nome: {cadastro["nome"]}')
    print(f'Idade: {cadastro["idade"]}')
    print(f'Carteira de Trabalho: {cadastro["ctps"]}')
    print(f'Ano de contratação: {cadastro["contratação"]}')
    print(f'Salário: {cadastro["salário"]}')
    print(f'Idade de aposentadoria: {cadastro["aposentadoria"]}')
else:
    print(cadastro)
    print(f'Nome: {cadastro["nome"]}')
    print(f'Idade: {cadastro["idade"]}')
