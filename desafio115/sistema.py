from desafio115.lib.interface import  *
from desafio115.lib.arquivo import  *
from time import  sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criaArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Cadastrar novas pessoas
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho(' Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)