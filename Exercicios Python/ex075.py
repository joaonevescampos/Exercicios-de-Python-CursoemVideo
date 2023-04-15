tupla = (int(input('primeiro número: ')), int(input('Segundo número: ')),
         int(input('Terceiro número: ')),int(input('Quarto número: ')))

print(f'O número 9 foi digitado {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'Número 3 está na {tupla.index(3) + 1}ª posição.')
else:
    print('Não tem nunhum número 3.')
print(f'Números pares:  ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, ' ', end='')






