d = float(input('Qual distância da sua viagem em km? '))
if d <= 200:
    p = d * 0.5
    print('O preço da sua viagem é: R${:.2f}'.format(p))
else:
    p = d * 0.45
    print('O preço da sua viagem é: R${:.2f}'.format(p))