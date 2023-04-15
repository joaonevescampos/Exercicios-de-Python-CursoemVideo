nascimento = int(input('Qual ano você nasceu? '))
from datetime import date
anoatual = date.today().year
idade = anoatual - nascimento
if 0 < idade <= 9:
    print('Sua idade: {}. Você é MIRIM!'.format(idade))
elif 10 < idade <= 14:
    print('Sua idade: {}. Você é INFANTIL!'.format(idade))
elif 15 < idade <= 19:
    print('Sua idade: {}. Você é JUNIOR!'.format(idade))
elif idade == 20:
    print('Sua idade: {}. Você é SÊNIOR!'.format(idade))
else:
    print('Sua idade: {}. Você é MASTER!'.format(idade))