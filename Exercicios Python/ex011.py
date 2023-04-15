larg = float(input(print('Qual a largura da parede em metros?')))
alt = float(input(print('Qual a altura da parede em metros?')))
a = larg * alt
lt = a / 2
print('Para pintar uma parede de {:.2f} m2 de área \n é necessario {:.2f} litros de tinta'.format(a,lt))