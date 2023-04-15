n = int(input('Digite um número inteiro qualquer: '))
resto = n % 2
if resto == 0:
    print('O número {} é par.'.format(n))
else:
    print('O número {} é ímpar.'.format(n))
