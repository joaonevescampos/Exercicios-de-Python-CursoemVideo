def leiaInt(msg):
    while True:
        try:
            i = int(input(msg))
            if i < 1 or i > 3:
                print('\033[31mERRO! Digite uma das opções apresentadas! (1, 2 ou 3).\033[m')
            else:
                print('-'*40)
                return i

        except KeyboardInterrupt:
            print('\033[31m\nO usuário preferiu interromper o programa!O número inteiro é 0.\033[m')
            break
        except (ValueError, TypeError):
            print('\033[31mHouve um problema na leitura dos dados digitados! Tente novamente.\033[m')


def leiaInt2(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except KeyboardInterrupt:
            print('\033[31m\nO usuário preferiu interromper o programa!O número inteiro é 0.\033[m')
            break
        except (ValueError, TypeError):
            print('\033[31mHouve um problema na leitura dos dados digitados! Tente novamente.\033[m')


def linha(tam=40):
    print('-' * tam)


def cabeçalho(titulo):
    linha()
    print(titulo.center(40))
    linha()


def menu(opcoes):
    cabeçalho('SISTEMA DE CADASTRO')
    c = 1
    for item in opcoes:
        print(f'{c} - {item}')
        c += 1
    linha()
    n = leiaInt('Sua opção: ')
    return n


