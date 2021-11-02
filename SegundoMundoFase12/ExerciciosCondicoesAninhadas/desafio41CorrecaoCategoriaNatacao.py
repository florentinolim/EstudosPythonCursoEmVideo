#A confederação nacional de natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categorias, de acordo com a idade:

# - Até 09 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 20 anos: Sênior
# - Acima: Master
from datetime import date, datetime
AnoAtual = date.today().year
Anonasc = int(input('informe o ano de nascimento:' ))
idade = AnoAtual - Anonasc
if idade <= 9:
    print('Atleta esta na categoria MIRIM {}'.format(idade))
elif idade <= 14:
    print('Atleta esta na categoria INFANTIL {}'.format(idade))
elif idade <= 19:
    print('Atleta esta na categoria JUNIOR {}'.format(idade))
elif idade <= 25:
    print('Atleta esta na categoria SÊNIOR {}'.format(idade))
else:
    print('Não pode praticar NATAÇÃO {} '.format(idade))

