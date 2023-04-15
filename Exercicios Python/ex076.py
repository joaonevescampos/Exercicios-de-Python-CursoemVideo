lista = ('Notebook', 3500, 'Smartphone',2500, 'Mouse', 50, 'Monitor', 1200, 'Teclado',500)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('='*40)
for c in range(0,10):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'R$ {lista[c]:>7.2f}')
print('='*40)