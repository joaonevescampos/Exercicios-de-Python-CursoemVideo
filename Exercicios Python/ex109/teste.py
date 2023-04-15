#programa principal
from ex109 import moeda
n = int(input('Digite um valor: '))
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'Um aumento de 10% de {moeda.moeda(n)} é {moeda.aumento(n, 10, True)}')
print(f'Uma redução de 8% de {moeda.moeda(n)} é {moeda.reduzir(n, 8, True)}')