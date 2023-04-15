gols = []
ficha = {}
sistema = []
soma = []
while True:
    ficha['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantidade de partidas: '))
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantidade de gols na {c}ª partida: ')))
        ficha['gols'] = gols[:]
    soma.append(sum(gols))
    ficha['soma'] = soma[:]
    sistema.append(ficha.copy())
    soma.clear()
    gols.clear()
    opcao = str(input('Quer continuar? '))
    print('-=' * 30)
    if opcao in 'Nn':
        break
print('-='*30)
print('{:<3}{:^10}{:^14}{:^3}'.format('nº','Nome','Gols', 'Total'))
for c in range(0, len(sistema)):
    print('{:<3}'.format(c + 1), end=' ')
    print('{:^10}'.format(sistema[c]['nome']), end=' ')
    print(' {}'.format(sistema[c]['gols']), end=' ')
    print('  {}'.format(sistema[c]['soma']), end=' ')
    print()

while True:
    print('-=' * 30)
    resp = int(input('Quer o relatório de qual jogador? (999 - parar). nº: '))
    if 0 < resp <= len(sistema):
        print(f'O {sistema[resp - 1]["nome"]} jogou {len(sistema[resp - 1]["gols"])} partidas.')
        for c in range(1, len(sistema[resp - 1]["gols"]) + 1):
            print(f'  => Na partida {c}, {sistema[resp - 1]["nome"]} fez {sistema[resp - 1]["gols"][c - 1]} gols.')
    elif resp == 999:
        print()
        print('-' * 17, ' OBRIGADO! VOLTE SEMPRE!', '-' * 17)
        break
    else:
        print('ERRO DE DIGITAÇÃO! Tente novamente!')
