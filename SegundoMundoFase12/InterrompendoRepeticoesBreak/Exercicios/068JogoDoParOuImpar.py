'''Faça um programa que jogue para ou impar com o computdor. O jogo só será inerrompido
quando o jogador PERDER mostrando o total de vitorias consecutivas que ele conquistou no final do jogo
'''
from random import randint
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 10)
    soma = computador + jogador
    tipo = ' '
    v = 0
    while tipo not in 'PI':
        tipo = str(input('Par ou impar [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} ', end= '')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÌMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
          print('VOCÊ PERDEU!')
          break
    elif tipo == 'I':
        if soma % 2 == 1:
           print('VOCE VENCEU')
           v += 1
        else:
            print('VOCÊ PERDEU')
            break
    print('Vamos Jogar novamente...')

print(f'GAME OVER! Você venceu {v} vezes.')




