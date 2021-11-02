'''Crie um programa que leia o nome e o preço de vários produtos.O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato
'''
total = totmil = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$ '))
    cont +=1
    total +=preco
    if preco > 1000:
         totmil +=1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = '  '
    while resp not in 'S/N':
        resp = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total gasto nessa compra foi de: {total:.2f}')
print(f'A quantidade de produtos Maiores que R$1000 são: {totmil}')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')