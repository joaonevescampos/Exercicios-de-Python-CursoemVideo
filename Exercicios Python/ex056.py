soma = 0
maisvelho = 0
nomevelho = ''
smenor = 0
for c in range(1, 5):
    nome = str(input('{}° nome: '.format(c))).strip().lower()
    idade = int(input('idade: '))
    sexo = str(input('sexo (M ou F): ')).strip().lower()
    soma = idade + soma

    if c == 1 and sexo == 'm' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    if sexo == 'm' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    if sexo == 'f' and idade < 20:
        smenor = smenor + 1
med = soma / c
print('-'*40)
print('O nome do homem mais velho é {} e ele tem {} anos.'.format(nomevelho, maisvelho))
print(' A média de idade é {} anos.'. format(med))
print('Tem {} mulher(es) abaixo de 20 anos'.format(smenor))

