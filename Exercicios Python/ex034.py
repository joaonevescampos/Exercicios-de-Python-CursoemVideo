s = float(input('Qual seu sálario? R$ '))
if s>= 1250:
    ns = s * 1.1
    print('Seu novo sálario com aumento de 10% é R${:.2f}.'.format(ns))
else:
    ns = s * 1.15
    print('Seu novo salário com aumento de 15% é R${:.2f}.'.format(ns))
