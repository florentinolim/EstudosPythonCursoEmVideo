'''
Melhore o jogo do desafio 28 onde o computador vai "pensar" em um numero entre 0 e 10.
Só que agora o jogador vai entrar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.
'''
from random import randint
computador = randint(0, 10)
jogador = False
cont = 0
while computador != jogador:
    jogador = int(input('Em que numero eu pensei?'))
    if jogador == computador:
        print('Você acertou'.format(computador, jogador))
    else:
        print('Você errou tente novamente')
        cont += 1
print('você acertou com {} vezes'.format(cont))
