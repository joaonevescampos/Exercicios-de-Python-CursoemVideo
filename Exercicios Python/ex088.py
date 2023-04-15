print('-'*30)
print('{:^30}'.format("JOGO DA MEGA SENA"))
print('-'*30)
n = int(input('Quantos jogos deseja sortear? '))
from random import randint
from time import sleep
jogo = []
for c in range(0, n):
    a = 0
    while a < 6:
        sorteio = randint(0, 60)
        jogo.append(sorteio)
        if jogo.count(jogo[a]) >= 2:
            jogo.remove(jogo[a])
            a -= 1
        a += 1
    sleep(1)
    jogo.sort()
    print(jogo)
    jogo.clear()
print('{:-^30}'.format('BOA SORTE!'))
