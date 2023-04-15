#programa principal
from ex107 import moeda
n = int(input('Digite um valor: '))
print(f'A metade de {n} é {moeda.metade(n)}')
print(f'O dobro de {n} é {moeda.dobro(n)}')
print(f'Um aumento de 10% de {n} é {moeda.aumento(n, 10)}')
print(f'Uma redução de 8% de {n} é {moeda.reduzir(n, 8)}')