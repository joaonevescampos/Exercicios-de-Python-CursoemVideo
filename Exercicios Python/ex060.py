
num = int(input('Digite um número inteiro: '))
a = num
fatorial = 1
while num != 1:
    fatorial = fatorial * num
    num = num - 1
print('{}! = {}'.format(a, fatorial))
