dados = list()
tot = list()
cont = pesado = leve = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    tot.append(dados[:])
    dados.clear()
    if cont == 0:
        leve = pesado = tot[0][1]
    if tot[cont][1] > pesado:
        pesado = tot[cont][1]
    if tot[cont][1] < leve:
        leve = tot[cont][1]
    cont += 1
    opcao = str(input('Quer continuar? '))
    if opcao in 'Nn':
        break

print(f'Ao todo, {cont} pessoas se cadastraram!')
print(f'O mais pesado pesa {pesado}. Peso de: ', end='')
for c in tot:
    if c[1] == pesado:
        print(c[0], ' ', end='')
print()
print(f'O mais leve pesa {leve}. Peso de: ', end='')
for c in tot:
    if c[1] == leve:
        print(c[0], ' ', end='')
