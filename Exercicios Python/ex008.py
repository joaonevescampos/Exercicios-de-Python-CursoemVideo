m = float(input('Digite o valor em metros'))
cm = m*100
mm = m*1000
print('{} metros equivale a {:.2f} cm'.format(m,cm),end = ' ')
print('ou {:.2f} mm.'.format(mm))