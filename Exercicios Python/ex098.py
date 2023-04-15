def contador(a, b, c):
    if c == 0:
        c = 1
    if a < b:
        while a <= b:
            sleep(0.5)
            print(a, end=' ')
            a = a + c
        a -= c
        print()

    if a > b:
        if c > 0:
            c = c * (-1)
        while a >= b:
            sleep(0.5)
            print(a, end=' ')
            a = a + c
        print()

from time import sleep
contador(1, 10, 1)
contador(10, 0, 2)
#personalização
inicio = int(input('Qual o primeiro elemento? '))
ultimo = int(input('Qual o último elemento? '))
razao = int(input('Qual passo? '))
contador(inicio, ultimo, razao)
