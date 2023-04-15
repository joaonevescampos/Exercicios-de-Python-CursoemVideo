num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um numero (999 - parar): '))
    cont += 1
    soma += num
    if num == 999:
        cont = cont - 1
        soma = soma - 999
print ('\033[33mVocê digitou {} números. A soma entre eles é: {}.'.format(cont, soma))

