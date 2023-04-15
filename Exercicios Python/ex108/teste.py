#programa principal
from ex108 import moeda
n = int(input('Digite um valor: '))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'Um aumento de 10% de {moeda.moeda(n)} é {moeda.moeda(moeda.aumento(n, 10))}')
print(f'Uma redução de 8% de {moeda.moeda(n)} é {moeda.moeda(moeda.reduzir(n, 8))}')