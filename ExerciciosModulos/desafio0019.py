#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
print('='*100)
print('Importando todas as bibliotecas ! ')

import random
aluno1 = str(input('Informe o primeiro aluno !'))
aluno2 = str(input('Informe o segundo aluno !'))
aluno3 = str(input('Informe o terceito aluno !'))
aluno4 = str(input('Informe o qurto aluno !'))

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
print('='*100)
print('Importando apenas as bibliotecas necessárias')
from random import choice

n1 = str(input('Informe o primeiro aluno !'))
n2 = str(input('Informe o segundo aluno !'))
n3 = str(input('Informe o terceito aluno !'))
n4 = str(input('Informe o qurto aluno !'))

lista2 = [n1, n2, n3, n4]
escolhido2 = choice(lista2)
print('O aluno escolhido foi {}'.format(escolhido2))