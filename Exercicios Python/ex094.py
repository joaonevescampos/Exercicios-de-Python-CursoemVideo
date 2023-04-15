dados = dict()
total = list()
p = soma = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: ').strip().upper())
    dados['idade'] = int(input('Idade: '))
    total.append(dados.copy())
    soma += dados['idade']
    p += 1
    opcao = str(input('Quer continuar? ')).strip().upper()
    if opcao in 'N':
        break
print('-='*30)
print(f'Há {p} pessoas cadastradas.')
print('A média entre as idades é: {:.1f}'.format(soma/ p))
print('As mulheres são: ', end='')

for c in range(0, p):
    if total[c]['sexo'] == 'F':
        print(f'{total[c]["nome"]}', end=' ')
print()
print('As pessoas acima da média de idade são: ', end='')
for c in range(0, p):
    if total[c]['idade'] > soma/p:
        print(f'{total[c]["nome"]} com {total[c]["idade"]} anos. ', end=' ')
print('-='*30)
