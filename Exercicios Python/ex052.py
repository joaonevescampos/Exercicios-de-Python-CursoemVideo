n = int(input('Digite um número qualquer: '))
a = 0
for p in range(2, n):
    if n % p == 0:
        print('\033[31mNão é primo!')
        a = 1
        break
if a == 0:
    print('\033[32mÉ primo!')





