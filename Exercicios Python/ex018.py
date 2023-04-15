import math
from math import tan, cos, sin, pi
a = float(input('Digite o ângulo desejado: '))
x = math.radians(a)
sen = sin(x)
cos = cos(x)
tan = tan(x)
print('sen({}°) = {:.2f} \n cos({}°) = {:.2f} \n tan({}°) = {:.2f}'.format(a,sen,a,cos,a,tan))