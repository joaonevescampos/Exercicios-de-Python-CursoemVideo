valores = ['a']
opcao = 'S'
b= 0
for v in valores:
    while opcao not in 'N':
        valores.append(int(input('Valor: ')))
        if 'a' in valores:
            valores.remove('a')
        if valores.count(valores[b]) == 1:
            print('Valor adicionado com sucesso!')
        else:
            valores.remove(valores[b])
            b -= 1
            print('Valor duplicado! Tente Novamente.')

        opcao = input('Quer continuar? ').upper().strip()
        b +=1
print(sorted(valores))






