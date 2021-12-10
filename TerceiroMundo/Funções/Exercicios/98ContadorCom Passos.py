'''Faça um programa que tenha uma função chamada contador(), que receba três
parametros inicio, fim e passo e realiza a contagem.

Seu programa tem que realizar três contagens através da função criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada .
'''
# i, f, p = Inicio fim e passo
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' *20)
    print(f'Contagem de {i} até {f}, de {p} e, {p}')
    sleep(2.5)


    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ',flush=True)
            sleep(0.5)
            cont -= p
        print('FIM"')



#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' *20)
print('Agora é a sua vez de personalizar a oontagem!')
ini = int(input('Inicio:     '))
fim = int(input('Fim       '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
