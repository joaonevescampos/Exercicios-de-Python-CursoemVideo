opcao = 'a'
menornome = ''
total = m1000 = menor = cont = 0
while opcao not in 'N':
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço do produto: '))
    total += valor
    cont += 1
    opcao = 'a'
    while opcao not in 'SN':
        opcao = str(input('Vai continuar? [S/N]: ')).strip().upper()[0]
    if valor > 1000:
        m1000 += 1
    if cont == 1:
        menor = valor
    else:
        if valor < menor:
            menor = valor
            menornome = nome
print(f'O total gasto é {total}.')
print(f'{m1000} produtos custam mais de R$1000,00.')
print(f'Produto mais barato foi: {menornome}.')



