def leiaInt(msg):
    while True:
        try:
            i = int(input(msg))
            print(f'\033[32mParabéns, você digitou o número inteiro: {i}\033[m')
            break

        except KeyboardInterrupt:
            print('\033[31m\nO usuário preferiu interromper o programa!O número inteiro é 0.\033[m')
            break
        except (ValueError, TypeError):
            print('\033[31mHouve um problema na leitura dos dados digitados! Tente novamente.\033[m')


def leiafloat(msg2):
    while True:
        try:
            r = float(input(msg2))
            print(f'\033[32mParabéns, você digitou o número real: {r}\033[m')
            break

        except KeyboardInterrupt:
            print(f'\033[31m\nO usuário preferiu interromper o programa!O número real é 0\033[m')
            break
        except (ValueError, TypeError):
            print('\033[31mHouve um problema na leitura dos dados digitados! Tente novamente.\033[m')


leiaInt('Digite um número inteiro: ')
leiafloat('Digite um número real: ')