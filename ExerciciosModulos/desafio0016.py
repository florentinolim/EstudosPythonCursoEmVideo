# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Exemplo =  digite um numero: 6.127
# O numero 6.127 tem a parte inteira 6
print('Importando todas as funcionalidades de math pra solucionar este exercicio.')
print('='*100)
import math
num = float(input('informe um numero real! '))
print('O valor digitado foi {} ea sua porção inteira é {}'.format(num, math.trunc(num)))

print('=' * 100)
print('Utilizando apenas o metodo especifico')
from math import trunc
print('A porção inteira  de {} é {}'.format(num, trunc(num)))

print('=' * 100)
print('Utilizando apenas a função interna do python desta forma não é necessário importar modulos')
print('O valor dgitado foi {} e a sua porção inteira novamente foi de {}'.format(num, int(num)))