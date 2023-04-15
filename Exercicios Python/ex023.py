numero = (input('Digite um número de até 4 dígitos:'))
o = numero.strip()
a = o.split()
l = a[0]
qze = 4 - len(l)
b = '0'* qze + a[0]
j = b.split()
print('Unidade:{}'.format(j[0][3]))
print('Dezena:{}'.format(j[0][2]))
print('Centena:{}'.format(j[0][1]))
print('Milhar:{}'.format(j[0][0]))



