dados = dict()
from random import randint
from time import sleep
dados['jogador1'] = randint(1, 6)
dados['jogador2'] = randint(1, 6)
dados['jogador3'] = randint(1, 6)
dados['jogador4'] = randint(1, 6)

print(f'Jogador 1: {dados["jogador1"]}')
sleep(1)
print(f'Jogador 2: {dados["jogador2"]}')
sleep(1)
print(f'Jogador 3: {dados["jogador3"]}')
sleep(1)
print(f'Jogador 4: {dados["jogador4"]}')
sleep(1)
sorted(dados.values())

print(sorted(dados.keys()) and sorted(dados.values()))
