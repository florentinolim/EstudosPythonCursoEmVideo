#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O Segundo Valor é maior
# - Não existe valor maior, os dois são iguais

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
if num1 > num2:
    print('O numero {} é maior que o {}'.format(num1, num2))
elif num2 > num1:
    print('O numero {} é maior que o numero {}'.format(num2, num1))
else:
    print('Os numeros {} e {} são iguais'.format(num1, num2))