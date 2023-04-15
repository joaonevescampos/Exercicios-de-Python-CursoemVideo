import urllib
import urllib.request
try:
    urllib.request.urlopen('http://pudim.com.br')
except:
    print('\033[31mNão consegui acessar o site!')
else:
    print('\033[32mConsegui acessar o site com sucesso!')