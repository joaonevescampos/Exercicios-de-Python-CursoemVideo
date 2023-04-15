
#metade
def metade(n=0, f=False):
    d = n / 2
    if f is True:
        return moeda(d)
    else:
        return d



#dobro
def dobro(n=0, f=False):
    m = n * 2
    if f is True:
        return moeda(m)
    else:
        return m


#aumento
def aumento(n=0, p=0, f=False):
    a = n * (100 + p)/ 100
    if f is True:
        return moeda(a)
    else:
        return a


#reduzir
def reduzir(n=0, p=0, f=False):
    r = n * (100 - p)/ 100
    if f is True:
        return moeda(r)
    else:
        return r

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n, aum=10, dim=8):
    return \
    print(f"""A metade de {moeda(n)} é {metade(n, True)}
O dobro de {moeda(n)} é {dobro(n, True)}
Um aumento de {aum}% de {moeda(n)} é {aumento(n, aum, True)}
Uma redução de {dim}% de {moeda(n)} é {reduzir(n, dim, True)}""")
