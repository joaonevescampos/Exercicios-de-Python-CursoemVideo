total = [[], []]
for c in range(0, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        total[0].append(num)
    else:
        total[1].append(num)

print(f'Lista completa: {total}')
print(f'Pares em ordem crescente: {sorted(total[0])}')
print(f'Impares em ordem crescente: {sorted(total[1])}')
