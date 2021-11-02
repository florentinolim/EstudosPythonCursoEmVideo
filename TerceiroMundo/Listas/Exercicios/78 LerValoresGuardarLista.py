'''Faça um programa que leia 5 valores numéricos e guarde em uma lista.
No final mostre qual foi o maior e o menor valor
Mostrando suas respectivas posições.'''
valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print('-=' * 40)
print(f'\n Os valores Digitados são: {valores}')
print(f' O Maior valor é {max(valores)}, e sua posição na lista é a {valores.index(max(valores))+1}')
print(f' O Menor valor é {min(valores)}, e a sua posição na lista é a {valores.index(min(valores))+1}')
print('-=' * 40)

