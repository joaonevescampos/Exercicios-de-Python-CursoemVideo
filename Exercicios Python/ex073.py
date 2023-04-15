tabela = ('palmeiras','internacional','fluminense','corinthians','flamengo','athletico-PR','atlético-MG','fortaleza','são paulo','américa')

print(f'5 primeiros colocados: {tabela[:5]}')
print(f'4 últimos colocados: {tabela[6:]}')
print(f'Ordem alfabética: {sorted(tabela)}')
f = tabela.index('fortaleza')
print(f'Fortaleza está na posicão {f + 1}')