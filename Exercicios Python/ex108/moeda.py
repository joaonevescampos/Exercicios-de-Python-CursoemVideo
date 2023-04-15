
#metade
def metade(n=0):
    d = n / 2
    return d


#dobro
def dobro(n=0):
    m = n * 2
    return m


#aumento
def aumento(n=0, p=0):
    a = n * (100 + p)/ 100
    return a


#reduzir
def reduzir(n=0, p=0):
    r = n * (100 - p)/ 100
    return r

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')