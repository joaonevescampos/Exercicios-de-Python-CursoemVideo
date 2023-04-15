soma = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        soma = soma + impar
print('A soma de todos ímpares e múltiplos de 3 é: {}.'.format(soma))