'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
num = (int(input('Digite um numero:')),
           int(input('Digite outro numero:')),
           int(input('Digite mais um numero:')),
           int(input('Digite o ultímo numero:')))
print(f'Você digitou o valor nove: {num.count(9)}')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição')
else:
    print('O numero três não aparece em nenhuma posição, pois não foi digitado.')
print('Os numeros pares são:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

