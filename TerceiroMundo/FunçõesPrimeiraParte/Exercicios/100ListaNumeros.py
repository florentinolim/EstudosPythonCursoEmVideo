'''Faça um programa que tenha uma lista chamada números e duas funções chamda sorteia()
e somapar(). A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda
função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior
'''
from random import randint
from time import sleep
def sorteia(lista):
      print('Sorteando cinco valores da lista: ', end=' ')
      for cont in range(0, 5):
            n = randint(1, 10)
            lista.append(n)
            print(f'{n}' , end=' ', flush=True)
            sleep(0.3)
      print('PRONTO')

def somapar(lista):
      soma = 0
      for valor in lista:
            if valor % 2 == 0:
                 soma += valor
      print(f'Somando os valores pares de {lista}, temos {soma}')


def somaimpar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 1:
            soma += valor
    print(f'Somando os valores impares de {lista}, temos {soma}')

#Programa principal
numeros = list()
sorteia(numeros)
somapar(numeros)
somaimpar(numeros)
