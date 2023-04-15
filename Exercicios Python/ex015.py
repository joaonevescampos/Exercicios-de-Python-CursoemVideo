km = float(input(print('Quantos km percorridos?')))
dia = int(input(print('Quantos dias alugou o carro?')))
p = 60 * dia + 0.15 * km
print('O preço a pagar é de R${:.2f}'.format(p))