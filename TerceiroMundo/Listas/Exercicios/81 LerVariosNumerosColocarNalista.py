'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois mostre:
A) Quantos numeros foram digitados.
B) A lista de valores, ordenada de forma descrescente
C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = list()
count = 0
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    count += 1
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Deseja continuar [S/N] ')).upper().strip()
    if resp == 'N':
       break
if 5 in lista:
        print('O valor 5 esta na lista')
else:
        print('O valor 5 não foi digitado')
print(f'Foi digitado {count} numeros')
lista.sort(reverse=True)
print(lista)
