opcao = 4
while opcao == 4:
    r = 0
    soma = 0
    multiplicar = 1
    maior = 0
    for c in range(1, 3):
        r = int(input('Digite o {}° valor: '.format(c)))
        soma += r
        multiplicar = multiplicar * r
        if r > maior:
            maior = r
    while opcao != 5:
        print('-'* 40)
        print('Escolha uma opção:')
        print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4]Novos números\n[5]Sair do programa ')
        opcao = int(input('opção: '))
        print('-' * 40)

        if opcao == 1:
            print('\033[33mA soma é {}.\033[m'.format(soma))
        if opcao == 2:
            print('\033[33mA multiplicação é: {}.\033[m'.format(multiplicar))
        if opcao == 3:
            print('\033[33mO maior número é: {}.\033[m'.format(maior))
        if opcao == 4:
            break
        if opcao == 5:
            print('\033[31mFIM DO PROGRAMA!')










