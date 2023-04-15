
nome = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
opcao = 'S'

while opcao in 'S':
    num = int(input('Digite um número de 0 a 20: '))
    if num < 0 or num > 20:
        num = int(input('Você digitou errado, tente novamente: '))
    else:
        print(f'Você digitou o número {nome[num]}.')
        opcao = str(input('Quer continuar?[S/N]: ')).upper().strip()
print('OBRIGADO! VOLTE SEMPRE!')



