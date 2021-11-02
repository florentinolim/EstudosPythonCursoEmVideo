'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que
estão na tupla.'''

'''from random import sample
num = tuple(sample(range(1), 5))
print(num)'''
'''from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')'''

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os numeros sorteados são: {}'.format(numeros))
for i in (numeros):
    print(i, end=' ')
print('\nO maior numero é {}'.format(max(numeros)))
print('O menor numero é {}'.format(min(numeros)))






