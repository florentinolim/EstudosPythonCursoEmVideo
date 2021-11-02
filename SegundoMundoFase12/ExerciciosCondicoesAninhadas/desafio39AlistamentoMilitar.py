#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# -Se ele ainda vai se alistar.
# -Se é a hora de se alistar.
# -Se já passou do tempo de alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date, datetime
anoAtual = date.today().year
anoNasc = int(input('Informe o ano de nascimento: '))
idade = anoAtual -anoNasc
print('Quem nasceu em {} tem {} anos em {}'.format(anoNasc, idade, anoAtual))
if idade == 18:
    print('Você tem que se alistar imediatamente {}'.format(idade))
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = anoAtual + saldo
    print('Seu alistamento será {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = anoAtual - saldo
    print('Passou da data de alistamento a {} anos atrás, seu ano de alistamento foi {}'.format(saldo, ano))


