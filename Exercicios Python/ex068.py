opcao = ''
pc = ''
cont = 0
print('\033[33m{:^40}\033[m'.format('JOGO PAR OU ÍMPAR'))
print('-'*40)
while True:
    opcao = str(input('Quer par ou ímpar? [P/I]: ')).upper().strip()[0]
    if opcao == 'P':
        pc = 'I'
    elif opcao == 'I':
        pc = 'P'
    else:
        while opcao != 'P' and opcao != 'I':
            opcao = str(input('Você digitou errado! Digite I ou P: ')).upper().strip()[0]
            if opcao == 'P':
                pc = 'I'
            elif opcao == 'I':
                pc = 'P'

    num = int(input('Faça sua jogada [0 a 10]: '))
    from random import randint
    chutepc = randint(0, 10)
    soma = chutepc + num

    if soma % 2 == 0:
        if opcao == 'P':
            print('\033[32mVOCÊ GANHOU!\033[m')
            print(f'Você jogou {num} e o PC {chutepc}. Soma foi {soma}')
            cont += 1
        if opcao == 'I':
            print('\033[31mVOCÊ PERDEU!\033[m')
            print(f'Você jogou {num} e o PC {chutepc}. Soma foi {soma}')
            print(f'\033[35mVocê teve {cont} vitórias consecutivas\033[m')
            print('\033[31mGAME OVER')
            break

    if soma % 2 != 0:
        if opcao == 'I':
            print('\033[32mVOCÊ GANHOU!\033[m')
            print(f'Você jogou {num} e o PC {chutepc}. Soma foi {soma}')
            cont += 1
        if opcao == 'P':
            print('\033[31mVOCÊ PERDEU!\033[m\n')
            print(f'Você jogou {num} e o PC {chutepc}. Soma foi {soma}')
            print(f'\033[35mVocê teve {cont} vitórias consecutivas\033[m')
            print('\033[31mGAME OVER')
            break
print('-'*40)

