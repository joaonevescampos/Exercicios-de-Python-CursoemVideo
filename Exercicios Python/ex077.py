lista = ('paralelepipedo', 'feijao','farofa', 'biscoito','batata')

for palavra in lista:
    print(f'\nNa palavra \033[1m{palavra.upper()}\033[m temos:',end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end='')


