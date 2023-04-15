nome = input(print('Qual seu nome?'))
n1 = float(input(print('Qual foi a sua primeira nota?')))
n2 = float(input(print('Qual foi a sua segunda nota?')))
print('Olá {}, a sua média é {:.2f}'.format(nome,(n1 + n2)/2))