#Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import
# no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando
# módulos built-in e módulos externos, oferecidos no Pypi.
print('='*100)
print('Importando todas as bibliotecas do modulo math e calculando a raiz quadrada usando sqrt')
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print ('A raiz de {} é igual a {} arredondando para cima com math.ceil'.format(num, math.ceil(raiz)))
print ('A raiz de {} é igual a {} arredondando para baixo com math.floor'.format(num, math.floor(raiz)))
print ('A raiz de {} é igual a {:.2f} arredondando utlizando a formatação de 2 casas decimais'.format(num, raiz))

print('='*100)
print('Importanto apenas o metodo sqrt e o floor')
from math import sqrt, floor
raiz2 = sqrt(num)
print(' A raiz de {} é igual a {:.2f}'.format(num, floor(raiz2)))
