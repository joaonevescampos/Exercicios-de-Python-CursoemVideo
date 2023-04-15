peso = float(input('Qual seu peso em kg? '))
altura = float(input('Qual sua altura em m? '))

imc = peso/(altura)**2

if imc < 18.5:
    print('\033[31m Seu IMC é : {:.2f}. Você está abaixo do peso! Come meu filho!\033[m'.format(imc))
elif 18.5 <= imc < 25:
    print('\033[32m Seu IMC é : {:.2f}. Você está no seu peso ideal! PARABÉNS!\033[m'.format(imc))
elif 25 <= imc < 30:
    print('\033[33m Seu IMC é : {:.2f}. Você está acima do peso! Vai emagrecer querido!\033[m'.format(imc))
else:
    print('\033[31m Seu IMC é : {:.2f}. Você está obeso mórbido! Deve emagrecer urgentemente!\033[m'.format(imc))

