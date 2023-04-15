print('\033[35m {:^45}\033[m'.format('JOKENPÔ'))
print('-'*45)
jogador = str(input('PEDRA, PAPEL OU TESOURA? '))
jogador = jogador.replace('.','').upper().strip()

from time import sleep
print('JO',end =''), sleep(1)
print(' KEN',end =''), sleep(1)
print(' PÔ!!!'), sleep(0.3)

lista = ['PEDRA', 'PAPEL', 'TESOURA']
from random import choice
pc = choice(lista)

if pc == jogador:
    print( '\033[33mEMPATE!\033[m')
elif pc == 'PEDRA' and jogador == 'TESOURA':
    print('\033[31mVOCÊ PERDEU!\033[m')
elif pc == 'PEDRA' and jogador == 'PAPEL':
    print('\033[32mVOCÊ GANHOU!\033[m')
elif pc == 'TESOURA' and jogador == 'PEDRA':
    print('\033[32mVOCÊ GANHOU!\033[m')
elif pc == 'TESOURA' and jogador == 'PAPEL':
    print('\033[31mVOCÊ PERDEU!\033[m')
elif pc == 'PAPEL' and jogador == 'TESOURA':
    print('\033[32mVOCÊ GANHOU!\033[m')
elif pc == 'PAPEL' and jogador == 'PEDRA':
    print('\033[31mVOCÊ PERDEU!\033[m')
else:
    print('\033[31mERRO! VOCÊ DIGITOU ERRADO! TENTE NOVAMENTE!')

print( '\033[33mVocê escolheu: {} e o computador: {}!\033[m'.format(jogador, pc))
print('-'*45)