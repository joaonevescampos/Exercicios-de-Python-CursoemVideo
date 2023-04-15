from random import randint
pc = randint(0,10)
print('{:^50}'.format('\033[35mJOGO DE ADIVINHAÇÃO\033[m'))
print('-'*50)
cont = 0
chute = 11
while chute != pc:
    chute = int(input('Adivinhe o número de 0 a 10 que estou pensando: '))
    cont += 1
    if chute != pc:
        print('\033[31mERROU! Tente Novamente!\033[m')
    else:
        print('\033[32mPARABÉNS! Você acertou depois de {} tentativas\033[m'.format(cont))
print('-'*50)