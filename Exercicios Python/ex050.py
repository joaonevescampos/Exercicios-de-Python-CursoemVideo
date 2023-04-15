soma = 0
for n in range(0,6):
    num = int(input('Digite um número: '))
    if num % 2 == 1:
        soma = soma + num
print('A soma dos números ímpares é: {}'.format(soma))