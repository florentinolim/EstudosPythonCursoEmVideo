'''Crie um codigo em pythom que teste se o site Pudim está acessivelpelo computador usado'''
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não esta acessivel no momento.')
else:
    print('Consegui acessar o sie Pudim com sucesso!')
    #print(site.read()) #Pega o conteúdo html do site