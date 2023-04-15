def sorteio(*num):
    for c in range(0, 5):
        lista.append(randint(0, 9))
    print(lista)


def somaPar(*num):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(soma)


lista = []
from random import randint
sorteio(lista)
somaPar(lista)
