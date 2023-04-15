from ex115.funcoes import *
from ex115.cadastro import *
from time import sleep
arq = 'cadastrodepessoas.txt'
if not arquivoExiste('cadastrodepessoas.txt'):
    criarArquivo('cadastrodepessoas.txt')
while True:
    n = menu(['Ver usuários cadastrados', 'Cadastrar novo usuário', 'Sair'])
    print(f'{f"OPÇÃO {n} escolhida"}')
    if n == 1:
        lerArquivo(arq)
        sleep(2)
    elif n == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt2('Idade: ')
        cadastro(arq, nome, idade)
        sleep(2)
    else:
        break


