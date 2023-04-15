def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            break
        print('\033[31mERRO! Número inválido. Tente novamente.\033[m')
    return n


n = leiaInt('Digite um número inteiro: ')
print(f'\033[32mVocê digitou o número inteiro {n}.')
