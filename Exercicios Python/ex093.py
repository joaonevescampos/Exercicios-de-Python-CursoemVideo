gols = []
ficha = {}
ficha['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantidade de partidas: '))
for c in range(1, partidas + 1):
    gols.append(int(input(f'Quantidade de gols na {c}ª partida: ')))
ficha['gols'] = gols
ficha['total'] = sum(gols)
print('-='*30)
print(ficha)
print('-='*30)
print(f'Nome: {ficha["nome"]}')
print(f'gols: {ficha["gols"]}')
print(f'Total de gols: {ficha["total"]}')
print('-='*30)
print(f'O {ficha["nome"]} jogou {partidas} partidas.')
for c in range(1, partidas + 1):
    print(f'  => Na partida {c}, {ficha["nome"]} fez {gols[c - 1]} gols.')
