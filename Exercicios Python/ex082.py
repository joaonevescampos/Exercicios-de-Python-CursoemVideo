numeros = []
pares = []
impares = []
opcao = 'S'
c = 0
while opcao not in 'N':
    numeros.append(int(input('Digite um valor: ')))
    opcao = str(input('Quer continuar? {S/N]: ')).upper().strip()
    if numeros[c] % 2 == 0:
        pares.append(numeros[c])
    else:
        impares.append(numeros[c])
    c += 1
print('-='* 20)
print(f'Todos os números: {numeros}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')
