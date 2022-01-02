'''Crie um pacote chamado utilidades CEV que tenha dois módulos internos chamados moeda e dado
 transfira todas as funções que nos utiizamos nos desafios 107, 108, e 109 para o primeiro pacote
  e mantenha tudo funcionando'''

#Podemos usar o parametro True False ou Vazio 
from desafio111.utilidadescev import  moeda

valor = float(input('Digite um valor: '))
#moeda.resumo(valor)
moeda.resumo(valor, 35, 22)