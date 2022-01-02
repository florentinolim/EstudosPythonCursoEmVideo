'''Adapte o código do desafio 107, criando uma função adicional chamao moeda que consiga mostrar os
 valores como um valor monetário formatado'''

import  moeda

valor = float(input('Digite um valor: '))
print(f'Preço de {moeda.moeda(valor)}  é {moeda.moeda(moeda.aumetar(valor, 10))}')
print(f'Preço de {moeda.moeda(valor)} com 10% a menos é: {moeda.moeda(moeda.diminuir(valor, 10))}')
print(f'A metade de {moeda.moeda(valor)} é: {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é: {moeda.moeda(moeda.dobro(valor))}')