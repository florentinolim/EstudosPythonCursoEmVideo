'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo,
cadastrando tudo em uma unica lista composta'''
from random import randint
from time import sleep
lista = list()
jogos = list()
qtnumeros = 0
print('-' * 30)
print('-     JOGOS DA MEGA SENA     ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
qtnumeros = int(input('Quantos numeros por cartão? '))
valor = float(input('Informe o valor de cada jogo '))
total = quant * valor
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= qtnumeros:
           break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'  SORTEANDO {quant} JOGOS ',  '-=' * 3)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
print(f'Total a pagar R${total}')



