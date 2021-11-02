'''Escreava um programa que faça o cmputador "pensar" em um número entre 0 e 5 e peça
para o usuário tentar descobrie qual foi o numero escolhido pelo conmputador
O programa devera escrever na telase o usuário venceu ou perdeu '''
import random
nuser = int(input('Infome o numero: '))
ncomp = random.randint(0, 5)
print(ncomp)
if nuser == ncomp:
    print('Usuário informou o numero {} e ACERTOU o numero {}'.format(nuser, ncomp))
else:
    print('Usuário unformou o numero {} e ERROU o correto é {}'.format(nuser, ncomp))


