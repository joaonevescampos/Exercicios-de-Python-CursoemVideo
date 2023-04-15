nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))

media = (nota1 + nota2)/2

if nota1 < 0 or nota2 < 0 or nota1 > 10 or nota2 > 10:
    print('\033[31m HOUVE UM ERRO NA SUA DIGITAÇÃO. SUA NOTA DEVE SER ENTRE 0 E 10.\033[m')
elif 0 < media < 4.9:
    print('\033[31m Infelizmente, você está reprovado!\033[m')
elif 5 < media < 6.9:
    print('\033[33m Você está de recuperação! Estude mais!\033[m')
elif 7 < media < 10:
    print('\033[32m Você está aprovado! PARABÉNS! :)\033[m')
else:
    print('\033[31m HOUVE UM ERRO NA SUA DIGITAÇÃO. SUA NOTA DEVE SER ENTRE 0 E 10.\033[m')
