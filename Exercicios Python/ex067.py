while True:
    n = int(input('Quer tabuada de qual número? '))
    if n < 0:
        print('FIM DO PROGRAMA!')
        break
    c = 0
    while c != 10:
        r = n * c
        c += 1
        print(f'{n} x {c} = {r}')
