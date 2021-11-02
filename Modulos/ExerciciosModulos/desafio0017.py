#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
print('='*100)
print('Usando o metodo matematico ')

cato = float(input('Digite o comprimento do cateto oposto! '))
cata = float(input('Digite o comprimento do cateto adjacente! '))
hipo = (cato **2 + cata **2) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(hipo))

print('='*100)
print('Importando todas as bibliotecas')
import math
print('='*100)
hipo2 = math.hypot(cato, cata)
print('O valor da hipotenusa é {:.2f}'.format(math.hypot(hipo2)))

print('='*100)
print('Importando apenas as bibliotecas necessárias')
from math import hypot
hipo3 = hypot(cato, cata)
print('O valor da hipotenusa é{:.2f}'.format(hypot(hipo3)))




