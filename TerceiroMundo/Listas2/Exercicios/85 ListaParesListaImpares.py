'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma unica
lista,que mantenha separados os valores pares e os valores impares.No final, mostre os valores pares e
impares em ordem crescente
'''
valor = 0
num = [[], []] # Declarando uma lista dentro da outra
for n in range(1, 8):
    valor = int(input(f'Digite o {n}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Todos os valores da lista são {num}')
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')
print('-=' * 30)
