
cont50 = cont20 = cont10 = cont1 = 0
n = int(input('Qual valor você deseja sacar? '))
while n > 0:
    cont50 += 1
    n = n - 50
cont50 = cont50 - 1
n = n + 50
while n > 0:
    cont20 += 1
    n = n - 20
cont20 = cont20 - 1
n = n + 20
while n > 0:
    cont10 += 1
    n = n - 10
cont10 = cont10 - 1
n = n + 10
while n > 0:
    cont1 += 1
    n = n - 1
print('-'*40)
if cont50 > 0:
    print(f'Total de {cont50} cédulas de R$50.')
if cont20 > 0:
    print(f'Total de {cont20} cédulas de R$20.')
if cont10 > 0:
    print(f'Total de {cont10} cédulas de R$10.')
if cont1 > 0:
    print(f'Total de {cont1} cédulas de R$1.')
print('-'*40)




