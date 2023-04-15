nome = str(input('Escreva um nome completo: ')).strip()
n = nome.split()
print('Primeiro nome é: {}'.format(n[0]))
print('Último nome é: {}'.format(n[len(n)-1]))


