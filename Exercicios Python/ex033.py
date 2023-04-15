
n1 = float(input('Qual primeiro número? '))
n2 = float(input('Qual segundo número? '))
n3 = float(input('Qual terceiro número? '))

if n1 > n2 > n3:
    print('{} é o maior número e {} é o menor.'.format(n1,n3))
if n1 > n3 > n2:
    print('{} é o maior número e {} é o menor.'.format(n1,n2))
if n2 > n1 > n3:
    print('{} é o maior número e {} é o menor.'.format(n2,n3))
if n2 > n3 > n1:
    print('{} é o maior número e {} é o menor.'.format(n2,n1))
if n3 > n2 > n1:
    print('{} é o maior número e {} é o menor.'.format(n3,n1))
if n3 > n1 > n2:
    print('{} é o maior número e {} é o menor.'.format(n3,n2))