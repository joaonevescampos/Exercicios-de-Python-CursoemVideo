decimal = int(input('Escreva um número inteiro qualquer: '))
print('\033[35mESCOLHA A BASE DE CONVERSÃO:\033[m')
print("""1. Binário \n2. Octal \n3. Hexadecimal""")
base = int(input('opção: '))

if base == 1:
    binario = bin(decimal)
    binario = binario.replace('0b','')
    print('\033[33m{} em binário é: {}.'.format(decimal,binario))
elif base == 2:
    octal = oct(decimal)
    octal = octal.replace('0o','')
    print('\033[33m{} em octal é: {}.'.format(decimal,octal))
elif base == 3:
    hexa = hex(decimal)
    hexa = hexa.replace('0x','')
    print('\033[33m{} em hexadecimal é: {}.'.format(decimal, hexa))

