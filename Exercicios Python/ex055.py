maispesado = 0
maisleve = 0
for pesos in range(0, 5):
    peso = float(input('Qual seu peso? '))
    if pesos == 1:
        maispesado = peso
        maisleve = peso
    else:
        if peso > maispesado:
            maispesado = peso
        if peso < maisleve:
            maisleve = peso

print('O mais pesado é {}kg e o mais leve pesa {}kg.'.format(maispesado, maisleve))



