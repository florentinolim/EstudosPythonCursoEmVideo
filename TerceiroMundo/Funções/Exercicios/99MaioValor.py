'''Faça um programa que tenha uma função chamada maior(), que receba vários
 parâmetros com valores inteiros.Seu programa tem que analisar todos os valores e dizer qual deles é o maior'''
from  time import sleep
def titulo(txt):
    print('-=' *30)
    print(txt)
    print('-=' * 30)
def maior(* num):
   cont = maior = 0
  # print('\nAnalisando os valores passados... ')
   for valor in num:
         print(f'{valor} ', end=' ',  flush=True)
         sleep((0.3))
         if cont == 0:
             maior = valor
         else:
             if valor > maior:
                 maior = valor
         cont +=1
   print(f'Foram informados {cont} valores ao todo')
   print(f'O maior valor informado foi {maior}.')




#Programa principal
print()
titulo('Analisando os valores passados')
maior(2, 4, 6, 8)
maior(1, 3, 5, 7)
maior(2, 6, 8,10)
maior(6)
maior()















