#Crie um programa que leia o ano de nascimento de 7 pessoas.
# No final mostre quantas pessoas ainda não atigiram a maior idade
#E quantos já são maiores
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('A {}º pessoa nasceu em ?'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor +=1
print('Numero de pessoas MAIOR IDADE SÃO: {}'.format(totmaior))
print('Numero de pessoas MENOR IDADE SÃO: {}'.format(totmenor))
