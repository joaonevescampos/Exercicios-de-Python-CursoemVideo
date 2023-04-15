import time
print('-'*40)
print('CALCULADORA DE FINANCIAMENTO DE IMÓVEL')
print('-'*40)
casa = float(input('\033[33m Qual o preço do imóvel que deseja financiar? R$\033[m'))
salario = float(input('\033[33m Qual seu salário líquido? R$\033[m'))
tempo = float(input('\033[33m Em quantos anos deseja quitar o imóvel?\033[m '))
prestacao = casa/(tempo * 12)
porcentagem = 100 * prestacao/salario
print('PROCESSANDO...')
time.sleep(3)
if porcentagem > 30:
    print('\033[31m Infelizmente, não será possível você financiar este imóvel. A prestação é de {:.2f}% do seu salário.\033[m'.format(porcentagem))
else:
    print('\033[32m PARABÉNS! Você poderá financiar essa casa pagando {:.2f}% do seu salário mensal.\033[m'.format(porcentagem))