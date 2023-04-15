opcao = 'S'
num = []
while True:
    num.append(int(input('Digite um valor: ')))
    opcao = str(input('QUer continuar? [S/N]: ')).upper().strip()
    if opcao == 'N':
        break
print(f'A lista tem {len(num)} elementos!')
num.sort(reverse=True)
print(f'A lista em ordem decrescente é: {num}')
if 5 in num:
    print('Tem "5" na lista!')
else:
    print('Não tem "5" na lista')
