p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 0
while cont != 10:
    print(p,' ', end='')
    p = p + r
    cont += 1
