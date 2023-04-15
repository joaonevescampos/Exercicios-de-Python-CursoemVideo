valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite o número na posição {c}: ')))

print(f'O maior valor é {max(valores)} e está na posição:', end='')

for c, v in enumerate(valores):
    if v == max(valores):
        print(f'{c}... ', end='')
print(f'\nO menor valor é {min(valores)} e está na posição:', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f'{c}... ', end='')
