i = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão? '))
decimo = i + (10 - 1)* r
print('A sequência segundo esses dados é:')
for pa in range(i, decimo + r, r):
    print(pa)

