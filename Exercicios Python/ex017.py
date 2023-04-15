import math
#from math import sqrt
cop = float(input('Qual o cateto oposto?'))
cad = float(input('Qual o cateto adjacente?'))
#h = sqrt(pow(cop,2) + pow(cad,2))
h = math.hypot(cop,cad)
print('O valor da hipotenusa é: {}'.format(h))