tmaior18 = h = m20 = 0
while True:
    sexo = opcao = 'a'
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]: ')).upper().strip()[0]
    idade = int(input('Idade: '))
    while opcao not in 'NS':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if sexo == 'M':
            h += 1
        if idade > 18:
            tmaior18 += 1
        if sexo == 'F' and idade < 20:
            m20 += 1
    if opcao == 'N':
        break
print(f'Tem {h} homens cadastrados, {tmaior18} pessoas acima de 18 anos e {m20} mulheres abaixo de 20 anos.')


