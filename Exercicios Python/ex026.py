frase = input('Escreva qualque frase: ')
print('Aparece a letra "a" {} vezes.'.format(frase.count('a')))
print('O "a" aparece a primeira vez na posição: {}.'.format(frase.find('a')))
print('O último aparece na posição: {}.'.format(frase.rfind('a')))