sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Você digitou errado. Digite M ou F, por gentileza!')
print('OBRIGADO!')