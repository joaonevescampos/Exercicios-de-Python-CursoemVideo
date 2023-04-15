print('\033[36m{:^44}\033[m'.format('TABUADA DE 0 A 10'))
print('-='*23)
num = int(input('Digite o número que deseja saber a tabuada: '))
for tabuada in range (0, 11):
    print('{:>19}'.format(tabuada), end ='')
    print (' x {} = '.format(num), end ='')
    r = tabuada * num
    print(r)
print('-='*23)