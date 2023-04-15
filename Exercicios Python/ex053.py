frase = str(input('Escreva uma frase qualquer: ')).lower().strip()
frase = frase.replace(' ', '')
tamanho = len(frase)
i = 0
for p in range(0, tamanho):
    i = (i + 1)
a = 0
i = i - 1
for p in range(0, tamanho):
    if frase[a] == frase[i - a]:
        a = a + 1
    else:
        print('\033[31mNão é um palíndromo!')
        break
if a == (i + 1):
    print('\033[32mÉ um palíndromo!')




