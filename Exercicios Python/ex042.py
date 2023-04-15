l1 = float(input('Qual o primeiro lado do triângulo? '))
l2 = float(input('Qual o segundo lado do triângulo? '))
l3 = float(input('Qual o terceiro lado do triângulo? '))
lista = [l1, l2, l3]
maior = max(lista)
somadosmenores = sum(lista) - max(lista)

if somadosmenores <= maior:
    print('\033[31m Não é possível formar um triângulo com esses segmentos!\033[m')
elif l1 == l2 == l3:
    print('Este triângulo é equilátero!')
elif (l1 == l2 or l1 == l3 or l2 == l3) and (l1 != l2 or l1 != l3 or l2 != l3):
    print('Este é um triângulo isósceles!')
else:
    print('Este é um triângulo escaleno!')
