from datetime import date
ano = date.today().year
maior = 0
menor = 0
for m in range(0, 7):
    nascimento = int(input('Qual ano você nasceu? '))
    idade = ano - nascimento
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

print('{} pessoas tem 18 anos ou mais e {} são menores de idade.'.format(maior, menor))