'''
Faça um programa que leia um numero e mostre o seu fatorial.
Ex
5!=5*4*3*2*1=120
'''
'''from math import factorial
num = int(input('Digite um numero: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))'''
'''
Metodo tradicional
'''
'''
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *=c
    c -=1
print('{}'.format(f))
'''
'''
Usando o For para calcular o fatorial
'''
n = int(input('Digite um numero: '))
c = n
f = 1
print('Calculando o fatorial: '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *=c
    c -=1
print('{}'.format(f))





