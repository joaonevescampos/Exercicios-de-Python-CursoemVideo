matriz = [[], [], []]
pares = []
for c in range(0, 9):
    if c <= 2:
        num = int(input(f'Digite o elemento (0,{c}): '))
        matriz[0].append(num)
        if num % 2 == 0:
            pares.append(num)
    if 3 <= c <= 5:
        num = int(input(f'Digite o elemento (1,{c - 3}): '))
        matriz[1].append(num)
        if num % 2 == 0:
            pares.append(num)
    if 6 <= c <= 8:
        num = int(input(f'Digite o elemento (2,{c - 6}): '))
        matriz[2].append(num)
        if num % 2 == 0:
            pares.append(num)

for a in range(0, 3):
    print(f'[ {matriz[0][a]} ] ', end='')
print()
for b in range(0, 3):
    print(f'[ {matriz[1][b]} ] ', end='')
print()
for d in range(0, 3):
    print(f'[ {matriz[2][d]} ] ', end='')
print()
print(f'A soma de todos os números pares é: {sum(pares)}')
print(f'A soma de todos elementos da terceira coluna é: {matriz[0][2] + matriz[1][2] +matriz[2][2]}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')

