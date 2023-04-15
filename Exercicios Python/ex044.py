produto = float(input('Qual o valor do produto? R$ '))
print('Como será o pagamento? ')
print('\033[33m DIGITE O NÚMERO DA OPÇÃO ESCOLHIDA\033[m')
pagamento = int(input("""1. À vista.
2. À vista no cartão.
3. Parcelado em 2x no cartão.
4. Parcelado em 3x no cartão.
\033[33m OPÇÃO ESCOLHIDA:\033[m """))

if pagamento == 1:
    produto = 0.8 * produto
    print('O produto comprado à vista é: R${:.2f}.'.format(produto))
elif pagamento == 2:
    produto = 0.9 * produto
    print('O produto comprado à vista no cartão é: R${:.2f}.'.format(produto))
elif pagamento == 3:
    produto = 0.95 * produto
    parcela = produto / 2
    print('O total a pagar parcelado em 2x é: R${:.2f}. Com cada parcela no valor de R${:.2f}.'.format(produto, parcela))
elif pagamento == 4:
    produto = 1.2 * produto
    n = int(input('Quantas parcelas?'))
    parcela = produto / n
    print('O total a pagar parcelado em {}x é: R${:.2f}. Com cada parcela no valor de R${:.2f}.'.format(n,produto, parcela))

