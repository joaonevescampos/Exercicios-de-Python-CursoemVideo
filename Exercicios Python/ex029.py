v = int(input('\033[1;36m Qual a velocidade do carro?\033[m '))
acima = v - 80
multa = 7 * acima
if v > 80:
    print("""\033[35m Seu carro foi multado no valor de:{}R${:.2f}{} \033[35m por estar 
    {} km/h acima da velocidade da via.""".format('\033[30;41m', multa,'\033[m', acima))
else:
    print('{} Tenha um bom dia, Dirija com segurança! {}'.format('\033[32m','\033[m'))