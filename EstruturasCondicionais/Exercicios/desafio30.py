#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR
num = int(input('Digite um numeto: '))
res = num % 2
if res == 0:
    print('O numero {} é par o resto da divisão é {}'.format(num, res))
else:
    print('O numero {} é impar o resto da divisão é {}'.format(num, res))

