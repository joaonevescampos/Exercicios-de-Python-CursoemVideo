p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 0
i = 1
a = 10
while cont != a:
    print(p,' ', end='')
    p = p + r
    cont += 1
while i != 0:
    i = int(input('\nQuer ver mais quantos termos? '))
    a = a + i
    while cont != a:
        print(p,' ', end='')
        p = p + r
        cont += 1
print('\033[33mFIM')
