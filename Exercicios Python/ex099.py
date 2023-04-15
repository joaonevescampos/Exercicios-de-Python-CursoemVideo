
def maior(*num):
    sleep(1)
    print(f'Lista: {num}')
    print(f'A lista tem {len(num)} números e o maior é: {max(num)}')
    print('-' * 30)

from time import sleep
maior(1, 20, 3, 6)
maior(2, 9, 53, 102, 86)
maior(33, 14)