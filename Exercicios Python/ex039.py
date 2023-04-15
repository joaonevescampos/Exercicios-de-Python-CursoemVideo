from datetime import date
nascimento = int(input('Em que ano nasceu? '))
anoatual = date.today().year
idade = anoatual - nascimento
if idade == 18:
    print('\033[35m Está na hora de se alistar, meu chapa! :)\033[m')
elif idade > 18:
    passou = idade - 18
    print('\033[31m Passou-se {} anos da hora de se alistar, meu velho! :(\033[m'.format(passou))
else:
    falta = 18 - idade
    print('\033[32m Faltam {} anos para se alistar, meu jovem!\033[m'.format(falta))
