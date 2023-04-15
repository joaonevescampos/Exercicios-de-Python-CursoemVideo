n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O \033[33m{}\033[m é o maior número'.format(n1))
elif n2 > n1:
    print('O \033[33m{}\033[m  é o maior número'.format(n2))
else:
    print('Os número \033[33m{}\033[m  e \033[33m{}\033[m  são iguais!'.format(n1,n2))