'''Crie um programa que chamado  moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro(), metade()'

Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
import  moeda

valor = float(input('Digite um valor: '))
print(f'Preço de R$ {valor} com 10% a mais é: {moeda.aumetar(valor, 10)}')
print(f'Preço de R$ {valor} com 10% a menos é: {moeda.diminuir(valor, 10)}')
print(f'A metade de R${valor} é: {moeda.metade(valor)}')
print(f'O dobro de R${valor} é: {moeda.dobro(valor)}')