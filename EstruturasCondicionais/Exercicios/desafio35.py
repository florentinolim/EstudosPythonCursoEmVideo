#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo
r1 = int(input('Informe a reta1:'))
r2 = int(input('Informe a reta2:'))
r3 = int(input('informe a reta3:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r1 + r2 :
    print('FORMA UM TRIANGULO'.format(r1, r2, r3))
else:
    print('NÃO FORMA O TRIANGULO')


