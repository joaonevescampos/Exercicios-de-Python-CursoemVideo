cores = {'pretoebranco':'\033[7m',
         'azulsub':'\033[4;34m',
         'limpa':'\033[m'}
from random import randint
from time import sleep
chutepc = randint(1,5)
chute = int(input('{} Chute um número de 1 a 5 que o pc escolheu:{} '.format(cores['pretoebranco'],cores['limpa'])))
print('PROCESSANDO...')
sleep(3)
print(chutepc)
if chutepc == chute:
    print('{}PARABÉNS! Você acertou o número que o pc escolheu!{}'.format(cores['azulsub'],cores['limpa']))
else:
    print('{}Que pena! Você errou o número!{} :('.format(cores['pretoebranco'],cores['limpa']))
