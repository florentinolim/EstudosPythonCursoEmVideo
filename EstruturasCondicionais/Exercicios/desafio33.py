#Faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if (n1 > n2) and (n1 > n3):
    print('O primeiro numero {} é maior que segundo numero {} e maior que terceiro numero {}'.format(n1, n2, n3))
elif (n2 > n1) and (n2 > n3):
    print('O segundo numero {} é maior que primeiro numero {} e maior que terceiro numero {}'.format(n2, n1, n3))
else:
    print('O terceiro numero {} é maior que segundo numero {} e maior que primeiro {}'.format(n3, n2, n1))

