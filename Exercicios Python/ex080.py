num = []
cont = inicio = c = 0
while c < 5:
    num.append(int(input('Digite um valor: ')))
    cont = num.count(num[c])
    if cont > 1:
        num.remove(num[c])
        print('\033[33mNão pode repetir o valor. Tente novamente!\033[m')
        c -= 1
    else:
        print('\033[32mValor registrado com sucesso!\033[m')
    if c == 0:
        inicio = c
    else:
        maior = max(num)
        menor = min(num)
        posicaomaior = num.index(maior)
        posicaomenor = num.index(menor)
        num.remove(maior)
        num.remove(menor)
        num.insert(c, maior)
        num.insert(inicio, menor)
        if c == 4:
            while True:
                if num[1] > num[2]:
                    num.insert(1, num[2])
                    del num[3]
                elif num[2] > num[3]:
                    num.insert(2, num[3])
                    del num[4]
                else:
                    break
    c += 1
print(f'lista ordenada: {num}')
