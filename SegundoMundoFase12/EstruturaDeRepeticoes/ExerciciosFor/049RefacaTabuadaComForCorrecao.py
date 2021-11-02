#Refaça o desafio009, mostrando a tabuada de um numero que o usuário escolher,
# so que agora usando um laço for.
num = int(input('Digite um numero: '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(num, c, num*c))
