r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
lista = [r1, r2, r3]
maior = max(lista)
soma = sum(lista) - max(lista)
if soma <= maior:
    print('Estes segmentos de reta não formam um triângulo!')
else:
    print('Estes segmentos de reta formam um triângulo!')
