'''Dentro do pacote UtilidadesCEV que criamos no desafio 111, temos um modulo chamado leiaDinheiro
qie seja capaz de funcionar como função input(), mas com uma validação de dados para aceitar apenas
valores que sejam monetários'''

#Podemos usar o parametro True False ou Vazio

from desafio112.utilidadescev import moeda
from desafio112.utilidadescev import dado

valor = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(valor, 35, 22)