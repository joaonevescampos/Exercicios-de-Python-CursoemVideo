def leiaDinheiro(msg):
    p = ''
    while True:
        p = str(input(msg)).strip().replace(',', '.')
        if p.isalpha():
            print(f'\033[31mErro! "{p}" inválido. Tente novamente!\033[m')
        else:
            p = float(p)
            break

    return p
