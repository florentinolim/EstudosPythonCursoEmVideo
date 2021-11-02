#Faça um programa que leia um ângulo qualquer e mostre na tela o
# valor do seno, cosseno e tangente desse ângulo
print('='*100)
print('Importanto todas as bibliotecas do modulo math')
import math
angulo = float(input('Digite o ângulo dque você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('A tangente de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

print('='*100)
print('Importanto apenas as bibliotecas necessarias')

from math import radians, sin, cos, tan
#angulo = float(input('Digite o ângulo dque você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente =  tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('A tangente de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
