opcao = 'S'
c = 0
sistema = [[],[],[]]
while opcao not in 'Nn':
    nome = str(input(f'{c + 1}º Nome: '))
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    sistema[0].append(nome)
    sistema[1].append(nota1)
    sistema[2].append(nota2)
    opcao = str(input('Quer continuar? '))
    c += 1
print('-'*24)
print('{:^24}'.format('BOLETIM DOS ALUNOS'))
print('-'*24)
print('Nº    Nome     Média ')
for cont in range(0, c):
    media = (sistema[1][cont] + sistema[2][cont])/ 2
    print('{}{:^14}{:^4.2f}'.format(cont,sistema[0][cont],media))

while True:
    parada = int(input('Deseja ver as notas de qual alunos? (999 - Finalizar): '))
    if parada == 999:
        print('OBRIGADO! VOLTE SEMPRE!')
        break
    elif parada < 0 or parada > cont:
        print('Você digitou errado! Tente novamente!')
    else:
        print(f'O aluno {sistema[0][parada]} tirou as notas: {sistema[1][parada]} e {sistema[2][parada]}.')
