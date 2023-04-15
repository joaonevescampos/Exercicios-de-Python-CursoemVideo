q = int(input('Digite a quantidade de termos da sequência de Fibonacci: '))
cont = 0
a0 = 0
a1 = 1
while cont != q:
     print(a0,' ', end = '')
     a1 = a0 + a1
     a0 = a1 - a0
     cont += 1

