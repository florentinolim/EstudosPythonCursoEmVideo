'''Modifique  as funções que foram criadas no desafio 107 para que elas aceitem um parametro
 a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda()
 desenvolvida no desafio 108'''

#Podemos usar o parametro True False ou Vazio

import moeda

valor = float(input('Digite um valor: '))
print(f'Preço aumentado em 10% é {moeda.moeda(valor)}  é {moeda.aumetar(valor, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(valor, 13, True)}')
print(f'Preço de {moeda.moeda(valor)} com 10% a menos é: {moeda.diminuir(valor, 10, True)}')
print(f'A metade de {moeda.moeda(valor)} é: {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é: {moeda.dobro(valor, True)}')