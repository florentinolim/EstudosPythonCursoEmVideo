'''Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista.No final, mostre
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves'''
pessoas = list()
dados = list()
pmaior = pmenor = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        pmaior = pmenor = dados[1]
    else:
        if dados[1] > pmaior:
            pmaior = dados[1]
        if dados[1] < pmenor:
            pmenor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar S/N'))
    if resp in 'Nn':
        break
print('-=' * 30)
#print(f'As pessoas cadastradas são: {pessoas}')
print(f'A quantidade de pessoas cadastradas foi: {len(pessoas)}')
print(f'O maior peso foi de : {pmaior} Kg. Peso de', end= ' ')
for p in pessoas:
    if p[1] == pmaior:
        print(f'[{p[0]}]', end='')
print()
print('-=' * 30)
print(f'O menor peso foi de : {pmenor} Kg. Peso de', end= ' ')
for p in pessoas:
    if p[1] == pmenor:
        print(f'[{p[0]}]', end='')
print()
print('-=' * 30)

