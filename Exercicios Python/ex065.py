r = ''
cont = 0
soma = 0
while r != 'N':
    num = int(input('Digite um número inteiro: '))
    r = str(input('Quer continuar [S/N]? ')).strip().upper()
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
media = soma/ cont

print('\033[33mA média dos valores digitados é: {}. O maior número é {} e o menor é {}.'.format(media, maior, menor))